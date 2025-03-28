from typing import Any, Literal, Union

from typing_extensions import NotRequired, TypedDict

import discord_typings

# THIS FILE HAS BEEN GENERATED AUTOMATICALLY FROM THE OFFICIAL DISCORD
# OPENAPI SPECIFICATION. REFER TO PROJECT DOCUMENTATION ON HOW TO RUN.
# DO NOT EDIT MANUALLY.

__all__: tuple[str, ...] = (
    'APIAccountResponse',
    'APIActionRowComponentForMessageRequest',
    'APIActionRowComponentForModalRequest',
    'APIActionRowComponentResponse',
    'APIActivitiesAttachmentResponse',
    'APIAfkTimeouts',
    'APIAllowedMentionTypes',
    'APIApplicationCommandAttachmentOption',
    'APIApplicationCommandAttachmentOptionResponse',
    'APIApplicationCommandAutocompleteCallbackRequest',
    'APIApplicationCommandBooleanOption',
    'APIApplicationCommandBooleanOptionResponse',
    'APIApplicationCommandChannelOption',
    'APIApplicationCommandChannelOptionResponse',
    'APIApplicationCommandCreateRequest',
    'APIApplicationCommandHandler',
    'APIApplicationCommandIntegerOption',
    'APIApplicationCommandIntegerOptionResponse',
    'APIApplicationCommandInteractionMetadataResponse',
    'APIApplicationCommandMentionableOption',
    'APIApplicationCommandMentionableOptionResponse',
    'APIApplicationCommandNumberOption',
    'APIApplicationCommandNumberOptionResponse',
    'APIApplicationCommandOptionIntegerChoice',
    'APIApplicationCommandOptionIntegerChoiceResponse',
    'APIApplicationCommandOptionNumberChoice',
    'APIApplicationCommandOptionNumberChoiceResponse',
    'APIApplicationCommandOptionStringChoice',
    'APIApplicationCommandOptionStringChoiceResponse',
    'APIApplicationCommandOptionType',
    'APIApplicationCommandPatchRequestPartial',
    'APIApplicationCommandPermission',
    'APIApplicationCommandPermissionType',
    'APIApplicationCommandResponse',
    'APIApplicationCommandRoleOption',
    'APIApplicationCommandRoleOptionResponse',
    'APIApplicationCommandStringOption',
    'APIApplicationCommandStringOptionResponse',
    'APIApplicationCommandSubcommandGroupOption',
    'APIApplicationCommandSubcommandGroupOptionResponse',
    'APIApplicationCommandSubcommandOption',
    'APIApplicationCommandSubcommandOptionResponse',
    'APIApplicationCommandType',
    'APIApplicationCommandUpdateRequest',
    'APIApplicationCommandUserOption',
    'APIApplicationCommandUserOptionResponse',
    'APIApplicationExplicitContentFilterTypes',
    'APIApplicationFormPartialDescription',
    'APIApplicationFormPartial',
    'APIApplicationIdentityProviderAuthType',
    'APIApplicationIncomingWebhookResponse',
    'APIApplicationIntegrationType',
    'APIApplicationIntegrationTypeConfiguration',
    'APIApplicationIntegrationTypeConfigurationResponse',
    'APIApplicationOAuth2InstallParams',
    'APIApplicationOAuth2InstallParamsResponse',
    'APIApplicationResponse',
    'APIApplicationRoleConnectionsMetadataItemRequest',
    'APIApplicationRoleConnectionsMetadataItemResponse',
    'APIApplicationTypes',
    'APIApplicationUserRoleConnectionResponse',
    'APIAttachmentResponse',
    'APIAuditLogActionTypes',
    'APIAuditLogEntryResponse',
    'APIAuditLogObjectChangeResponse',
    'APIAutomodActionType',
    'APIAutomodEventType',
    'APIAutomodKeywordPresetType',
    'APIAutomodTriggerType',
    'APIAvailableLocalesEnum',
    'APIBaseCreateMessageCreateRequest',
    'APIBasicApplicationResponse',
    'APIBasicMessageResponse',
    'APIBlockMessageAction',
    'APIBlockMessageActionMetadata',
    'APIBlockMessageActionMetadataResponse',
    'APIBlockMessageActionResponse',
    'APIBotAccountPatchRequest',
    'APIBulkBanUsersResponse',
    'APIButtonComponentForMessageRequest',
    'APIButtonComponentResponse',
    'APIButtonStyleTypes',
    'APIChannelFollowerResponse',
    'APIChannelFollowerWebhookResponse',
    'APIChannelPermissionOverwriteRequest',
    'APIChannelPermissionOverwriteResponse',
    'APIChannelPermissionOverwrites',
    'APIChannelSelectComponentForMessageRequest',
    'APIChannelSelectComponentResponse',
    'APIChannelSelectDefaultValue',
    'APIChannelSelectDefaultValueResponse',
    'APIChannelTypes',
    'APICommandPermissionResponse',
    'APICommandPermissionsResponse',
    'APIComponentEmojiForMessageRequest',
    'APIComponentEmojiResponse',
    'APIConfettiPotionCreateRequest',
    'APIConnectedAccountGuildResponse',
    'APIConnectedAccountIntegrationResponse',
    'APIConnectedAccountProviders',
    'APIConnectedAccountResponse',
    'APIConnectedAccountVisibility',
    'APICreateEntitlementRequestData',
    'APICreateForumThreadRequest',
    'APICreateGroupDMInviteRequest',
    'APICreateGuildChannelRequest',
    'APICreateGuildInviteRequest',
    'APICreateGuildRequestChannelItem',
    'APICreateGuildRequestRoleItem',
    'APICreateMessageInteractionCallbackRequest',
    'APICreateMessageInteractionCallbackResponse',
    'APICreateOrUpdateThreadTagRequest',
    'APICreatePrivateChannelRequest',
    'APICreateTextThreadWithMessageRequest',
    'APICreateTextThreadWithoutMessageRequest',
    'APICreatedThreadResponse',
    'APIDefaultKeywordListTriggerMetadata',
    'APIDefaultKeywordListTriggerMetadataResponse',
    'APIDefaultKeywordListUpsertRequest',
    'APIDefaultKeywordListUpsertRequestPartial',
    'APIDefaultKeywordRuleResponse',
    'APIDefaultReactionEmojiResponse',
    'APIDiscordIntegrationResponse',
    'APIEmbeddedActivityInstance',
    'APIEmbeddedActivityLocationKind',
    'APIEmojiResponse',
    'APIEntitlementOwnerTypes',
    'APIEntitlementResponse',
    'APIEntitlementTenantFulfillmentStatusResponse',
    'APIEntitlementTypes',
    'APIEntityMetadataExternal',
    'APIEntityMetadataExternalResponse',
    'APIEntityMetadataStageInstance',
    'APIEntityMetadataStageInstanceResponse',
    'APIEntityMetadataVoice',
    'APIEntityMetadataVoiceResponse',
    'APIExternalConnectionIntegrationResponse',
    'APIExternalScheduledEventCreateRequest',
    'APIExternalScheduledEventPatchRequestPartial',
    'APIExternalScheduledEventResponse',
    'APIFlagToChannelAction',
    'APIFlagToChannelActionMetadata',
    'APIFlagToChannelActionMetadataResponse',
    'APIFlagToChannelActionResponse',
    'APIForumLayout',
    'APIForumTagResponse',
    'APIFriendInviteResponse',
    'APIGatewayBotResponse',
    'APIGatewayBotSessionStartLimitResponse',
    'APIGatewayResponse',
    'APIGithubAuthor',
    'APIGithubCheckApp',
    'APIGithubCheckPullRequest',
    'APIGithubCheckRun',
    'APIGithubCheckRunOutput',
    'APIGithubCheckSuite',
    'APIGithubComment',
    'APIGithubCommit',
    'APIGithubDiscussion',
    'APIGithubIssue',
    'APIGithubRelease',
    'APIGithubRepository',
    'APIGithubReview',
    'APIGithubUser',
    'APIGithubWebhook',
    'APIGroupDMInviteResponse',
    'APIGuildAuditLogResponse',
    'APIGuildBanResponse',
    'APIGuildChannelLocation',
    'APIGuildChannelResponse',
    'APIGuildCreateRequest',
    'APIGuildExplicitContentFilterTypes',
    'APIGuildFeatures',
    'APIGuildHomeSettingsResponse',
    'APIGuildIncomingWebhookResponse',
    'APIGuildInviteResponse',
    'APIGuildMFALevel',
    'APIGuildMFALevelResponse',
    'APIGuildMemberResponse',
    'APIGuildNSFWContentLevel',
    'APIGuildOnboardingMode',
    'APIGuildOnboardingResponse',
    'APIGuildPatchRequestPartial',
    'APIGuildPreviewResponse',
    'APIGuildProductPurchaseResponse',
    'APIGuildPruneResponse',
    'APIGuildResponse',
    'APIGuildRoleResponse',
    'APIGuildRoleTagsResponse',
    'APIGuildScheduledEventEntityTypes',
    'APIGuildScheduledEventPrivacyLevels',
    'APIGuildScheduledEventStatuses',
    'APIGuildStickerResponse',
    'APIGuildSubscriptionIntegrationResponse',
    'APIGuildTemplateChannelResponse',
    'APIGuildTemplateChannelTags',
    'APIGuildTemplateResponse',
    'APIGuildTemplateRoleResponse',
    'APIGuildTemplateSnapshotResponse',
    'APIGuildWelcomeChannel',
    'APIGuildWelcomeScreenChannelResponse',
    'APIGuildWelcomeScreenResponse',
    'APIGuildWithCountsResponse',
    'APIIconEmojiResponse',
    'APIIncomingWebhookInteractionRequest',
    'APIIncomingWebhookRequestPartial',
    'APIIncomingWebhookUpdateForInteractionCallbackRequestPartial',
    'APIIncomingWebhookUpdateRequestPartial',
    'APIIntegrationApplicationResponse',
    'APIIntegrationExpireBehaviorTypes',
    'APIIntegrationExpireGracePeriodTypes',
    'APIIntegrationTypes',
    'APIInteractionApplicationCommandAutocompleteCallbackIntegerData',
    'APIInteractionApplicationCommandAutocompleteCallbackNumberData',
    'APIInteractionApplicationCommandAutocompleteCallbackStringData',
    'APIInteractionCallbackResponse',
    'APIInteractionCallbackTypes',
    'APIInteractionContextType',
    'APIInteractionResponse',
    'APIInteractionTypes',
    'APIInviteApplicationResponse',
    'APIInviteChannelRecipientResponse',
    'APIInviteChannelResponse',
    'APIInviteGuildResponse',
    'APIInviteStageInstanceResponse',
    'APIInviteTargetTypes',
    'APIInviteTypes',
    'APIKeywordRuleResponse',
    'APIKeywordTriggerMetadata',
    'APIKeywordTriggerMetadataResponse',
    'APIKeywordUpsertRequest',
    'APIKeywordUpsertRequestPartial',
    'APILaunchActivityInteractionCallbackRequest',
    'APILaunchActivityInteractionCallbackResponse',
    'APIListApplicationEmojisResponse',
    'APIListGuildSoundboardSoundsResponse',
    'APILobbyMemberRequest',
    'APILobbyMemberResponse',
    'APILobbyMessageResponse',
    'APILobbyResponse',
    'APIMLSpamRuleResponse',
    'APIMLSpamTriggerMetadata',
    'APIMLSpamTriggerMetadataResponse',
    'APIMLSpamUpsertRequest',
    'APIMLSpamUpsertRequestPartial',
    'APIMentionSpamRuleResponse',
    'APIMentionSpamTriggerMetadata',
    'APIMentionSpamTriggerMetadataResponse',
    'APIMentionSpamUpsertRequest',
    'APIMentionSpamUpsertRequestPartial',
    'APIMentionableSelectComponentForMessageRequest',
    'APIMentionableSelectComponentResponse',
    'APIMessageActivityResponse',
    'APIMessageAllowedMentionsRequest',
    'APIMessageAttachmentRequest',
    'APIMessageAttachmentResponse',
    'APIMessageCallResponse',
    'APIMessageComponentInteractionMetadataResponse',
    'APIMessageComponentTypes',
    'APIMessageCreateRequest',
    'APIMessageEditRequestPartial',
    'APIMessageEmbedAuthorResponse',
    'APIMessageEmbedFieldResponse',
    'APIMessageEmbedFooterResponse',
    'APIMessageEmbedImageResponse',
    'APIMessageEmbedProviderResponse',
    'APIMessageEmbedResponse',
    'APIMessageEmbedVideoResponse',
    'APIMessageInteractionResponse',
    'APIMessageMentionChannelResponse',
    'APIMessageReactionCountDetailsResponse',
    'APIMessageReactionEmojiResponse',
    'APIMessageReactionResponse',
    'APIMessageReferenceRequest',
    'APIMessageReferenceResponse',
    'APIMessageReferenceType',
    'APIMessageResponse',
    'APIMessageRoleSubscriptionDataResponse',
    'APIMessageSnapshotResponse',
    'APIMessageStickerItemResponse',
    'APIMessageType',
    'APIMetadataItemTypes',
    'APIMinimalContentMessageResponse',
    'APIModalInteractionCallbackRequest',
    'APIModalInteractionCallbackRequestData',
    'APIModalSubmitInteractionMetadataResponse',
    'APIMyGuildResponse',
    'APINameplatePalette',
    'APINewMemberActionResponse',
    'APINewMemberActionType',
    'APIOAuth2GetAuthorizationResponse',
    'APIOAuth2GetKeys',
    'APIOAuth2GetOpenIDConnectUserInfoResponse',
    'APIOAuth2Key',
    'APIOAuth2Scopes',
    'APIOnboardingPromptOptionRequest',
    'APIOnboardingPromptOptionResponse',
    'APIOnboardingPromptResponse',
    'APIOnboardingPromptType',
    'APIPartialDiscordIntegrationResponse',
    'APIPartialExternalConnectionIntegrationResponse',
    'APIPartialGuildSubscriptionIntegrationResponse',
    'APIPollAnswerCreateRequest',
    'APIPollAnswerDetailsResponse',
    'APIPollAnswerResponse',
    'APIPollCreateRequest',
    'APIPollEmoji',
    'APIPollEmojiCreateRequest',
    'APIPollLayoutTypes',
    'APIPollMedia',
    'APIPollMediaCreateRequest',
    'APIPollMediaResponse',
    'APIPollResponse',
    'APIPollResultsEntryResponse',
    'APIPollResultsResponse',
    'APIPongInteractionCallbackRequest',
    'APIPremiumGuildTiers',
    'APIPremiumTypes',
    'APIPrivateApplicationResponse',
    'APIPrivateChannelLocation',
    'APIPrivateChannelResponse',
    'APIPrivateGroupChannelResponse',
    'APIPrivateGuildMemberResponse',
    'APIProvisionalTokenResponse',
    'APIPurchaseNotificationResponse',
    'APIPurchaseType',
    'APIQuarantineUserAction',
    'APIQuarantineUserActionMetadata',
    'APIQuarantineUserActionMetadataResponse',
    'APIQuarantineUserActionResponse',
    'APIReactionTypes',
    'APIResolvedObjectsResponse',
    'APIResourceChannelResponse',
    'APIRichEmbed',
    'APIRichEmbedAuthor',
    'APIRichEmbedField',
    'APIRichEmbedFooter',
    'APIRichEmbedImage',
    'APIRichEmbedProvider',
    'APIRichEmbedThumbnail',
    'APIRichEmbedVideo',
    'APIRoleSelectComponentForMessageRequest',
    'APIRoleSelectComponentResponse',
    'APIRoleSelectDefaultValue',
    'APIRoleSelectDefaultValueResponse',
    'APISDKMessageRequest',
    'APIScheduledEventResponse',
    'APIScheduledEventUserResponse',
    'APISettingsEmojiResponse',
    'APISlackWebhook',
    'APISnowflakeSelectDefaultValueTypes',
    'APISortingOrder',
    'APISoundboardCreateRequest',
    'APISoundboardPatchRequestPartial',
    'APISoundboardSoundResponse',
    'APISoundboardSoundSendRequest',
    'APISpamLinkRuleResponse',
    'APISpamLinkTriggerMetadataResponse',
    'APIStageInstanceResponse',
    'APIStageInstancesPrivacyLevels',
    'APIStageScheduledEventCreateRequest',
    'APIStageScheduledEventPatchRequestPartial',
    'APIStageScheduledEventResponse',
    'APIStandardStickerResponse',
    'APIStickerFormatTypes',
    'APIStickerPackCollectionResponse',
    'APIStickerPackResponse',
    'APIStickerTypes',
    'APIStringSelectComponentForMessageRequest',
    'APIStringSelectComponentResponse',
    'APIStringSelectOptionForMessageRequest',
    'APIStringSelectOptionResponse',
    'APITeamMemberResponse',
    'APITeamMembershipStates',
    'APITeamResponse',
    'APITextInputComponentForModalRequest',
    'APITextInputComponentResponse',
    'APITextInputStyleTypes',
    'APIThreadAutoArchiveDuration',
    'APIThreadMemberResponse',
    'APIThreadMetadataResponse',
    'APIThreadResponse',
    'APIThreadSearchResponse',
    'APIThreadSearchTagSetting',
    'APIThreadSortOrder',
    'APIThreadSortingMode',
    'APIThreadsResponse',
    'APITypingIndicatorResponse',
    'APIUpdateDMRequestPartial',
    'APIUpdateDefaultReactionEmojiRequest',
    'APIUpdateGroupDMRequestPartial',
    'APIUpdateGuildChannelRequestPartial',
    'APIUpdateGuildOnboardingRequest',
    'APIUpdateMessageInteractionCallbackRequest',
    'APIUpdateMessageInteractionCallbackResponse',
    'APIUpdateOnboardingPromptRequest',
    'APIUpdateThreadRequestPartial',
    'APIUpdateThreadTagRequest',
    'APIUserAvatarDecorationResponse',
    'APIUserCollectiblesResponse',
    'APIUserCommunicationDisabledAction',
    'APIUserCommunicationDisabledActionMetadata',
    'APIUserCommunicationDisabledActionMetadataResponse',
    'APIUserCommunicationDisabledActionResponse',
    'APIUserGuildOnboardingResponse',
    'APIUserNameplateResponse',
    'APIUserNotificationSettings',
    'APIUserPIIResponse',
    'APIUserPrimaryGuildResponse',
    'APIUserResponse',
    'APIUserSelectComponentForMessageRequest',
    'APIUserSelectComponentResponse',
    'APIUserSelectDefaultValue',
    'APIUserSelectDefaultValueResponse',
    'APIVanityURLErrorResponse',
    'APIVanityURLResponse',
    'APIVerificationLevels',
    'APIVideoQualityModes',
    'APIVoiceRegionResponse',
    'APIVoiceScheduledEventCreateRequest',
    'APIVoiceScheduledEventPatchRequestPartial',
    'APIVoiceScheduledEventResponse',
    'APIVoiceStateResponse',
    'APIWebhookSlackEmbed',
    'APIWebhookSlackEmbedField',
    'APIWebhookSourceChannelResponse',
    'APIWebhookSourceGuildResponse',
    'APIWebhookTypes',
    'APIWelcomeMessageResponse',
    'APIWelcomeScreenPatchRequestPartial',
    'APIWidgetActivity',
    'APIWidgetChannel',
    'APIWidgetImageStyles',
    'APIWidgetMember',
    'APIWidgetResponse',
    'APIWidgetSettingsResponse',
    'APIWidgetUserDiscriminator',
)


class APIAccountResponse(TypedDict):
    id: str
    name: NotRequired[Union[str, None]]


class APIActionRowComponentForMessageRequest(TypedDict):
    type: Literal[1]
    components: list[Union['discord_typings.APIButtonComponentForMessageRequest', 'discord_typings.APIChannelSelectComponentForMessageRequest', 'discord_typings.APIMentionableSelectComponentForMessageRequest', 'discord_typings.APIRoleSelectComponentForMessageRequest', 'discord_typings.APIStringSelectComponentForMessageRequest', 'discord_typings.APIUserSelectComponentForMessageRequest']]


class APIActionRowComponentForModalRequest(TypedDict):
    type: Literal[1]
    components: list['discord_typings.APITextInputComponentForModalRequest']


class APIActionRowComponentResponse(TypedDict):
    type: Literal[1]
    id: int
    components: NotRequired[Union[list[Union['discord_typings.APIButtonComponentResponse', 'discord_typings.APIChannelSelectComponentResponse', 'discord_typings.APIMentionableSelectComponentResponse', 'discord_typings.APIRoleSelectComponentResponse', 'discord_typings.APIStringSelectComponentResponse', 'discord_typings.APITextInputComponentResponse', 'discord_typings.APIUserSelectComponentResponse']], None]]


class APIActivitiesAttachmentResponse(TypedDict):
    attachment: 'discord_typings.APIAttachmentResponse'


APIAfkTimeouts = Literal[
    60,
    300,
    900,
    1800,
    3600,
]


APIAllowedMentionTypes = Literal[
    'users',
    'roles',
    'everyone',
]


class APIApplicationCommandAttachmentOption(TypedDict):
    type: Literal[11]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandAttachmentOptionResponse(TypedDict):
    type: Literal[11]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandAutocompleteCallbackRequest(TypedDict):
    type: Literal[8]
    data: Union['discord_typings.APIInteractionApplicationCommandAutocompleteCallbackIntegerData', 'discord_typings.APIInteractionApplicationCommandAutocompleteCallbackNumberData', 'discord_typings.APIInteractionApplicationCommandAutocompleteCallbackStringData']


class APIApplicationCommandBooleanOption(TypedDict):
    type: Literal[5]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandBooleanOptionResponse(TypedDict):
    type: Literal[5]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandChannelOption(TypedDict):
    type: Literal[7]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    channel_types: NotRequired[Union[list['discord_typings.APIChannelTypes'], None]]


class APIApplicationCommandChannelOptionResponse(TypedDict):
    type: Literal[7]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    channel_types: NotRequired[Union[list['discord_typings.APIChannelTypes'], None]]


class APIApplicationCommandCreateRequest(TypedDict):
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    options: NotRequired[Union[list[Union['discord_typings.APIApplicationCommandAttachmentOption', 'discord_typings.APIApplicationCommandBooleanOption', 'discord_typings.APIApplicationCommandChannelOption', 'discord_typings.APIApplicationCommandIntegerOption', 'discord_typings.APIApplicationCommandMentionableOption', 'discord_typings.APIApplicationCommandNumberOption', 'discord_typings.APIApplicationCommandRoleOption', 'discord_typings.APIApplicationCommandStringOption', 'discord_typings.APIApplicationCommandSubcommandGroupOption', 'discord_typings.APIApplicationCommandSubcommandOption', 'discord_typings.APIApplicationCommandUserOption']], None]]
    default_member_permissions: NotRequired[Union[int, None]]
    dm_permission: NotRequired[Union[bool, None]]
    contexts: NotRequired[Union[list['discord_typings.APIInteractionContextType'], None]]
    integration_types: NotRequired[Union[list['discord_typings.APIApplicationIntegrationType'], None]]
    handler: NotRequired[Union[None, 'discord_typings.APIApplicationCommandHandler']]
    type: NotRequired[Union[None, 'discord_typings.APIApplicationCommandType']]


APIApplicationCommandHandler = Literal[
]


class APIApplicationCommandIntegerOption(TypedDict):
    type: Literal[4]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    autocomplete: NotRequired[Union[bool, None]]
    choices: NotRequired[Union[list['discord_typings.APIApplicationCommandOptionIntegerChoice'], None]]
    min_value: NotRequired[Union[None, int]]
    max_value: NotRequired[Union[None, int]]


class APIApplicationCommandIntegerOptionResponse(TypedDict):
    type: Literal[4]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    autocomplete: NotRequired[Union[bool, None]]
    choices: NotRequired[Union[list['discord_typings.APIApplicationCommandOptionIntegerChoiceResponse'], None]]
    min_value: NotRequired[Union[None, int]]
    max_value: NotRequired[Union[None, int]]


class APIApplicationCommandInteractionMetadataResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[2]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    authorizing_integration_owners: dict[str, 'discord_typings.APISnowflake']
    original_response_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    target_user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    target_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIApplicationCommandMentionableOption(TypedDict):
    type: Literal[9]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandMentionableOptionResponse(TypedDict):
    type: Literal[9]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandNumberOption(TypedDict):
    type: Literal[10]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    autocomplete: NotRequired[Union[bool, None]]
    choices: NotRequired[Union[list['discord_typings.APIApplicationCommandOptionNumberChoice'], None]]
    min_value: NotRequired[Union[float, None]]
    max_value: NotRequired[Union[float, None]]


class APIApplicationCommandNumberOptionResponse(TypedDict):
    type: Literal[10]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    autocomplete: NotRequired[Union[bool, None]]
    choices: NotRequired[Union[list['discord_typings.APIApplicationCommandOptionNumberChoiceResponse'], None]]
    min_value: NotRequired[Union[float, None]]
    max_value: NotRequired[Union[float, None]]


class APIApplicationCommandOptionIntegerChoice(TypedDict):
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    value: int


class APIApplicationCommandOptionIntegerChoiceResponse(TypedDict):
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    value: int


class APIApplicationCommandOptionNumberChoice(TypedDict):
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    value: float


class APIApplicationCommandOptionNumberChoiceResponse(TypedDict):
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    value: float


class APIApplicationCommandOptionStringChoice(TypedDict):
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    value: str


class APIApplicationCommandOptionStringChoiceResponse(TypedDict):
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    value: str


APIApplicationCommandOptionType = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
]


class APIApplicationCommandPatchRequestPartial(TypedDict):
    name: NotRequired[str]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    options: NotRequired[Union[list[Union['discord_typings.APIApplicationCommandAttachmentOption', 'discord_typings.APIApplicationCommandBooleanOption', 'discord_typings.APIApplicationCommandChannelOption', 'discord_typings.APIApplicationCommandIntegerOption', 'discord_typings.APIApplicationCommandMentionableOption', 'discord_typings.APIApplicationCommandNumberOption', 'discord_typings.APIApplicationCommandRoleOption', 'discord_typings.APIApplicationCommandStringOption', 'discord_typings.APIApplicationCommandSubcommandGroupOption', 'discord_typings.APIApplicationCommandSubcommandOption', 'discord_typings.APIApplicationCommandUserOption']], None]]
    default_member_permissions: NotRequired[Union[int, None]]
    dm_permission: NotRequired[Union[bool, None]]
    contexts: NotRequired[Union[list['discord_typings.APIInteractionContextType'], None]]
    integration_types: NotRequired[Union[list['discord_typings.APIApplicationIntegrationType'], None]]
    handler: NotRequired[Union[None, 'discord_typings.APIApplicationCommandHandler']]


class APIApplicationCommandPermission(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIApplicationCommandPermissionType'
    permission: bool


APIApplicationCommandPermissionType = Literal[
    1,
    2,
    3,
]


class APIApplicationCommandResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    application_id: 'discord_typings.APISnowflake'
    version: 'discord_typings.APISnowflake'
    default_member_permissions: NotRequired[Union[str, None]]
    type: 'discord_typings.APIApplicationCommandType'
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    dm_permission: NotRequired[Union[bool, None]]
    contexts: NotRequired[Union[list['discord_typings.APIInteractionContextType'], None]]
    integration_types: NotRequired[Union[list['discord_typings.APIApplicationIntegrationType'], None]]
    options: NotRequired[Union[list[Union['discord_typings.APIApplicationCommandAttachmentOptionResponse', 'discord_typings.APIApplicationCommandBooleanOptionResponse', 'discord_typings.APIApplicationCommandChannelOptionResponse', 'discord_typings.APIApplicationCommandIntegerOptionResponse', 'discord_typings.APIApplicationCommandMentionableOptionResponse', 'discord_typings.APIApplicationCommandNumberOptionResponse', 'discord_typings.APIApplicationCommandRoleOptionResponse', 'discord_typings.APIApplicationCommandStringOptionResponse', 'discord_typings.APIApplicationCommandSubcommandGroupOptionResponse', 'discord_typings.APIApplicationCommandSubcommandOptionResponse', 'discord_typings.APIApplicationCommandUserOptionResponse']], None]]
    nsfw: NotRequired[Union[bool, None]]


class APIApplicationCommandRoleOption(TypedDict):
    type: Literal[8]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandRoleOptionResponse(TypedDict):
    type: Literal[8]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandStringOption(TypedDict):
    type: Literal[3]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    autocomplete: NotRequired[Union[bool, None]]
    min_length: NotRequired[Union[int, None]]
    max_length: NotRequired[Union[int, None]]
    choices: NotRequired[Union[list['discord_typings.APIApplicationCommandOptionStringChoice'], None]]


class APIApplicationCommandStringOptionResponse(TypedDict):
    type: Literal[3]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    autocomplete: NotRequired[Union[bool, None]]
    choices: NotRequired[Union[list['discord_typings.APIApplicationCommandOptionStringChoiceResponse'], None]]
    min_length: NotRequired[Union[int, None]]
    max_length: NotRequired[Union[int, None]]


class APIApplicationCommandSubcommandGroupOption(TypedDict):
    type: Literal[2]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    options: NotRequired[Union[list['discord_typings.APIApplicationCommandSubcommandOption'], None]]


class APIApplicationCommandSubcommandGroupOptionResponse(TypedDict):
    type: Literal[2]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    options: NotRequired[Union[list['discord_typings.APIApplicationCommandSubcommandOptionResponse'], None]]


class APIApplicationCommandSubcommandOption(TypedDict):
    type: Literal[1]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    options: NotRequired[Union[list[Union['discord_typings.APIApplicationCommandAttachmentOption', 'discord_typings.APIApplicationCommandBooleanOption', 'discord_typings.APIApplicationCommandChannelOption', 'discord_typings.APIApplicationCommandIntegerOption', 'discord_typings.APIApplicationCommandMentionableOption', 'discord_typings.APIApplicationCommandNumberOption', 'discord_typings.APIApplicationCommandRoleOption', 'discord_typings.APIApplicationCommandStringOption', 'discord_typings.APIApplicationCommandUserOption']], None]]


class APIApplicationCommandSubcommandOptionResponse(TypedDict):
    type: Literal[1]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]
    options: NotRequired[Union[list[Union['discord_typings.APIApplicationCommandAttachmentOptionResponse', 'discord_typings.APIApplicationCommandBooleanOptionResponse', 'discord_typings.APIApplicationCommandChannelOptionResponse', 'discord_typings.APIApplicationCommandIntegerOptionResponse', 'discord_typings.APIApplicationCommandMentionableOptionResponse', 'discord_typings.APIApplicationCommandNumberOptionResponse', 'discord_typings.APIApplicationCommandRoleOptionResponse', 'discord_typings.APIApplicationCommandStringOptionResponse', 'discord_typings.APIApplicationCommandUserOptionResponse']], None]]


APIApplicationCommandType = Literal[
    1,
    2,
    3,
    4,
]


class APIApplicationCommandUpdateRequest(TypedDict):
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    options: NotRequired[Union[list[Union['discord_typings.APIApplicationCommandAttachmentOption', 'discord_typings.APIApplicationCommandBooleanOption', 'discord_typings.APIApplicationCommandChannelOption', 'discord_typings.APIApplicationCommandIntegerOption', 'discord_typings.APIApplicationCommandMentionableOption', 'discord_typings.APIApplicationCommandNumberOption', 'discord_typings.APIApplicationCommandRoleOption', 'discord_typings.APIApplicationCommandStringOption', 'discord_typings.APIApplicationCommandSubcommandGroupOption', 'discord_typings.APIApplicationCommandSubcommandOption', 'discord_typings.APIApplicationCommandUserOption']], None]]
    default_member_permissions: NotRequired[Union[int, None]]
    dm_permission: NotRequired[Union[bool, None]]
    contexts: NotRequired[Union[list['discord_typings.APIInteractionContextType'], None]]
    integration_types: NotRequired[Union[list['discord_typings.APIApplicationIntegrationType'], None]]
    handler: NotRequired[Union[None, 'discord_typings.APIApplicationCommandHandler']]
    type: NotRequired[Union[None, 'discord_typings.APIApplicationCommandType']]
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIApplicationCommandUserOption(TypedDict):
    type: Literal[6]
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


class APIApplicationCommandUserOptionResponse(TypedDict):
    type: Literal[6]
    name: str
    name_localized: NotRequired[Union[str, None]]
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localized: NotRequired[Union[str, None]]
    description_localizations: NotRequired[Union[dict[str, str], None]]
    required: NotRequired[Union[bool, None]]


APIApplicationExplicitContentFilterTypes = Literal[
    0,
    1,
]


class APIApplicationFormPartialDescription(TypedDict):
    default: str
    localizations: NotRequired[Union[dict[str, str], None]]


class APIApplicationFormPartial(TypedDict):
    description: NotRequired[Union['discord_typings.APIApplicationFormPartialDescription', None]]
    icon: NotRequired[Union[str, None]]
    cover_image: NotRequired[Union[str, None]]
    team_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    flags: NotRequired[Union[int, None]]
    interactions_endpoint_url: NotRequired[Union[str, None]]
    explicit_content_filter: NotRequired[Union[None, 'discord_typings.APIApplicationExplicitContentFilterTypes']]
    max_participants: NotRequired[Union[int, None]]
    type: NotRequired[Union[None, 'discord_typings.APIApplicationTypes']]
    tags: NotRequired[Union[list[str], None]]
    custom_install_url: NotRequired[Union[str, None]]
    install_params: NotRequired[Union[None, 'discord_typings.APIApplicationOAuth2InstallParams']]
    role_connections_verification_url: NotRequired[Union[str, None]]
    integration_types_config: NotRequired[Union[dict[str, Union[None, 'discord_typings.APIApplicationIntegrationTypeConfiguration']], None]]


APIApplicationIdentityProviderAuthType = Literal[
    'OIDC',
    'EPIC_ONLINE_SERVICES_ACCESS_TOKEN',
    'EPIC_ONLINE_SERVICES_ID_TOKEN',
    'STEAM_SESSION_TICKET',
    'UNITY_SERVICES_ID_TOKEN',
]


class APIApplicationIncomingWebhookResponse(TypedDict):
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    avatar: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    id: 'discord_typings.APISnowflake'
    name: str
    type: Literal[3]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


APIApplicationIntegrationType = Literal[
    0,
    1,
]


class APIApplicationIntegrationTypeConfiguration(TypedDict):
    oauth2_install_params: NotRequired[Union[None, 'discord_typings.APIApplicationOAuth2InstallParams']]


class APIApplicationIntegrationTypeConfigurationResponse(TypedDict):
    oauth2_install_params: NotRequired[Union[None, 'discord_typings.APIApplicationOAuth2InstallParamsResponse']]


class APIApplicationOAuth2InstallParams(TypedDict):
    scopes: NotRequired[Union[list[Literal['applications.commands', 'bot']], None]]
    permissions: NotRequired[Union[int, None]]


class APIApplicationOAuth2InstallParamsResponse(TypedDict):
    scopes: list[Literal['applications.commands', 'bot']]
    permissions: str


class APIApplicationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: str
    type: NotRequired[Union[None, 'discord_typings.APIApplicationTypes']]
    cover_image: NotRequired[Union[str, None]]
    primary_sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    bot: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    slug: NotRequired[Union[str, None]]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    rpc_origins: NotRequired[Union[list[Union[str, None]], None]]
    bot_public: NotRequired[Union[bool, None]]
    bot_require_code_grant: NotRequired[Union[bool, None]]
    terms_of_service_url: NotRequired[Union[str, None]]
    privacy_policy_url: NotRequired[Union[str, None]]
    custom_install_url: NotRequired[Union[str, None]]
    install_params: NotRequired[Union[None, 'discord_typings.APIApplicationOAuth2InstallParamsResponse']]
    integration_types_config: NotRequired[Union[dict[str, 'discord_typings.APIApplicationIntegrationTypeConfigurationResponse'], None]]
    verify_key: str
    flags: int
    max_participants: NotRequired[Union[int, None]]
    tags: NotRequired[Union[list[str], None]]


class APIApplicationRoleConnectionsMetadataItemRequest(TypedDict):
    type: 'discord_typings.APIMetadataItemTypes'
    key: str
    name: str
    name_localizations: NotRequired[Union[dict[str, Union[str, None]], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, Union[str, None]], None]]


class APIApplicationRoleConnectionsMetadataItemResponse(TypedDict):
    type: 'discord_typings.APIMetadataItemTypes'
    key: str
    name: str
    name_localizations: NotRequired[Union[dict[str, str], None]]
    description: str
    description_localizations: NotRequired[Union[dict[str, str], None]]


APIApplicationTypes = Literal[
    4,
]


class APIApplicationUserRoleConnectionResponse(TypedDict):
    platform_name: NotRequired[Union[str, None]]
    platform_username: NotRequired[Union[str, None]]
    metadata: NotRequired[Union[dict[str, str], None]]


class APIAttachmentResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    filename: str
    size: int
    url: str
    proxy_url: str
    width: NotRequired[Union[int, None]]
    height: NotRequired[Union[int, None]]
    duration_secs: NotRequired[Union[float, None]]
    waveform: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    content_type: NotRequired[Union[str, None]]
    ephemeral: NotRequired[Union[bool, None]]
    title: NotRequired[Union[str, None]]
    application: NotRequired[Union[None, 'discord_typings.APIApplicationResponse']]
    clip_created_at: NotRequired[Union[str, None]]
    clip_participants: NotRequired[Union[list['discord_typings.APIUserResponse'], None]]


APIAuditLogActionTypes = Literal[
    1,
    10,
    11,
    12,
    13,
    14,
    15,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    30,
    31,
    32,
    40,
    41,
    42,
    50,
    51,
    52,
    60,
    61,
    62,
    72,
    73,
    74,
    75,
    80,
    81,
    82,
    83,
    84,
    85,
    90,
    91,
    92,
    100,
    101,
    102,
    110,
    111,
    112,
    121,
    130,
    131,
    132,
    140,
    141,
    142,
    143,
    144,
    145,
    146,
    150,
    151,
    163,
    164,
    165,
    166,
    167,
    171,
    172,
    180,
    190,
    191,
    192,
    193,
    211,
]


class APIAuditLogEntryResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    action_type: 'discord_typings.APIAuditLogActionTypes'
    user_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    target_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    changes: NotRequired[Union[list['discord_typings.APIAuditLogObjectChangeResponse'], None]]
    options: NotRequired[Union[dict[str, str], None]]
    reason: NotRequired[Union[str, None]]


class APIAuditLogObjectChangeResponse(TypedDict):
    key: NotRequired[Union[str, None]]
    new_value: NotRequired[Any]
    old_value: NotRequired[Any]


APIAutomodActionType = Literal[
    1,
    2,
    3,
    4,
]


APIAutomodEventType = Literal[
    1,
    2,
]


APIAutomodKeywordPresetType = Literal[
    1,
    2,
    3,
]


APIAutomodTriggerType = Literal[
    1,
    2,
    3,
    4,
    5,
]


APIAvailableLocalesEnum = Literal[
    'ar',
    'bg',
    'cs',
    'da',
    'de',
    'el',
    'en-GB',
    'en-US',
    'es-419',
    'es-ES',
    'fi',
    'fr',
    'he',
    'hi',
    'hr',
    'hu',
    'id',
    'it',
    'ja',
    'ko',
    'lt',
    'nl',
    'no',
    'pl',
    'pt-BR',
    'ro',
    'ru',
    'sv-SE',
    'th',
    'tr',
    'uk',
    'vi',
    'zh-CN',
    'zh-TW',
]


class APIBaseCreateMessageCreateRequest(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    sticker_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    flags: NotRequired[Union[int, None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollCreateRequest']]
    confetti_potion: NotRequired[Union[None, 'discord_typings.APIConfettiPotionCreateRequest']]


class APIBasicApplicationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: str
    type: NotRequired[Union[None, 'discord_typings.APIApplicationTypes']]
    cover_image: NotRequired[Union[str, None]]
    primary_sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    bot: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


class APIBasicMessageResponse(TypedDict):
    type: 'discord_typings.APIMessageType'
    content: str
    mentions: list['discord_typings.APIUserResponse']
    mention_roles: list['discord_typings.APISnowflake']
    attachments: list['discord_typings.APIMessageAttachmentResponse']
    embeds: list['discord_typings.APIMessageEmbedResponse']
    timestamp: str
    edited_timestamp: NotRequired[Union[str, None]]
    flags: int
    components: list['discord_typings.APIActionRowComponentResponse']
    resolved: NotRequired[Union[None, 'discord_typings.APIResolvedObjectsResponse']]
    stickers: NotRequired[Union[list[Union['discord_typings.APIGuildStickerResponse', 'discord_typings.APIStandardStickerResponse']], None]]
    sticker_items: NotRequired[Union[list['discord_typings.APIMessageStickerItemResponse'], None]]
    id: 'discord_typings.APISnowflake'
    channel_id: 'discord_typings.APISnowflake'
    author: 'discord_typings.APIUserResponse'
    pinned: bool
    mention_everyone: bool
    tts: bool
    call: NotRequired[Union[None, 'discord_typings.APIMessageCallResponse']]
    activity: NotRequired[Union[None, 'discord_typings.APIMessageActivityResponse']]
    application: NotRequired[Union[None, 'discord_typings.APIBasicApplicationResponse']]
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    interaction: NotRequired[Union[None, 'discord_typings.APIMessageInteractionResponse']]
    nonce: NotRequired[Union[int, str, None]]
    webhook_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    message_reference: NotRequired[Union[None, 'discord_typings.APIMessageReferenceResponse']]
    thread: NotRequired[Union[None, 'discord_typings.APIThreadResponse']]
    mention_channels: NotRequired[Union[list[Union[None, 'discord_typings.APIMessageMentionChannelResponse']], None]]
    role_subscription_data: NotRequired[Union[None, 'discord_typings.APIMessageRoleSubscriptionDataResponse']]
    purchase_notification: NotRequired[Union[None, 'discord_typings.APIPurchaseNotificationResponse']]
    position: NotRequired[Union[int, None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollResponse']]
    interaction_metadata: NotRequired[Union['discord_typings.APIApplicationCommandInteractionMetadataResponse', 'discord_typings.APIMessageComponentInteractionMetadataResponse', 'discord_typings.APIModalSubmitInteractionMetadataResponse', None]]
    message_snapshots: NotRequired[Union[list['discord_typings.APIMessageSnapshotResponse'], None]]


class APIBlockMessageAction(TypedDict):
    type: Literal[1]
    metadata: NotRequired[Union[None, 'discord_typings.APIBlockMessageActionMetadata']]


class APIBlockMessageActionMetadata(TypedDict):
    custom_message: NotRequired[Union[str, None]]


class APIBlockMessageActionMetadataResponse(TypedDict):
    custom_message: NotRequired[Union[str, None]]


class APIBlockMessageActionResponse(TypedDict):
    type: Literal[1]
    metadata: 'discord_typings.APIBlockMessageActionMetadataResponse'


class APIBotAccountPatchRequest(TypedDict):
    username: str
    avatar: NotRequired[Union[str, None]]
    banner: NotRequired[Union[str, None]]


class APIBulkBanUsersResponse(TypedDict):
    banned_users: list['discord_typings.APISnowflake']
    failed_users: list['discord_typings.APISnowflake']


class APIButtonComponentForMessageRequest(TypedDict):
    type: Literal[2]
    custom_id: NotRequired[Union[str, None]]
    style: 'discord_typings.APIButtonStyleTypes'
    label: NotRequired[Union[str, None]]
    disabled: NotRequired[Union[bool, None]]
    url: NotRequired[Union[str, None]]
    sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji: NotRequired[Union[None, 'discord_typings.APIComponentEmojiForMessageRequest']]


class APIButtonComponentResponse(TypedDict):
    type: Literal[2]
    id: int
    custom_id: NotRequired[Union[str, None]]
    style: 'discord_typings.APIButtonStyleTypes'
    label: NotRequired[Union[str, None]]
    disabled: NotRequired[Union[bool, None]]
    emoji: NotRequired[Union[None, 'discord_typings.APIComponentEmojiResponse']]
    url: NotRequired[Union[str, None]]
    sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


APIButtonStyleTypes = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
]


class APIChannelFollowerResponse(TypedDict):
    channel_id: 'discord_typings.APISnowflake'
    webhook_id: 'discord_typings.APISnowflake'


class APIChannelFollowerWebhookResponse(TypedDict):
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    avatar: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    id: 'discord_typings.APISnowflake'
    name: str
    type: Literal[2]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    source_guild: NotRequired[Union[None, 'discord_typings.APIWebhookSourceGuildResponse']]
    source_channel: NotRequired[Union[None, 'discord_typings.APIWebhookSourceChannelResponse']]


class APIChannelPermissionOverwriteRequest(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: NotRequired[Union[None, 'discord_typings.APIChannelPermissionOverwrites']]
    allow: NotRequired[Union[int, None]]
    deny: NotRequired[Union[int, None]]


class APIChannelPermissionOverwriteResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIChannelPermissionOverwrites'
    allow: str
    deny: str


APIChannelPermissionOverwrites = Literal[
    0,
    1,
]


class APIChannelSelectComponentForMessageRequest(TypedDict):
    type: Literal[8]
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list['discord_typings.APIChannelSelectDefaultValue'], None]]
    channel_types: NotRequired[Union[list['discord_typings.APIChannelTypes'], None]]


class APIChannelSelectComponentResponse(TypedDict):
    type: Literal[8]
    id: int
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    channel_types: NotRequired[Union[list['discord_typings.APIChannelTypes'], None]]
    default_values: NotRequired[Union[list['discord_typings.APIChannelSelectDefaultValueResponse'], None]]


class APIChannelSelectDefaultValue(TypedDict):
    type: Literal['channel']
    id: 'discord_typings.APISnowflake'


class APIChannelSelectDefaultValueResponse(TypedDict):
    type: Literal['channel']
    id: 'discord_typings.APISnowflake'


APIChannelTypes = Literal[
    1,
    3,
    0,
    2,
    4,
    5,
    10,
    11,
    12,
    13,
    14,
    15,
]


class APICommandPermissionResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIApplicationCommandPermissionType'
    permission: bool


class APICommandPermissionsResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    application_id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    permissions: list['discord_typings.APICommandPermissionResponse']


class APIComponentEmojiForMessageRequest(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    name: str


class APIComponentEmojiResponse(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    name: str
    animated: NotRequired[Union[bool, None]]


class APIConfettiPotionCreateRequest(TypedDict):
    pass


class APIConnectedAccountGuildResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]


class APIConnectedAccountIntegrationResponse(TypedDict):
    id: str
    type: 'discord_typings.APIIntegrationTypes'
    account: 'discord_typings.APIAccountResponse'
    guild: 'discord_typings.APIConnectedAccountGuildResponse'


APIConnectedAccountProviders = Literal[
    'battlenet',
    'bluesky',
    'bungie',
    'ebay',
    'epicgames',
    'facebook',
    'github',
    'instagram',
    'mastodon',
    'leagueoflegends',
    'paypal',
    'playstation',
    'reddit',
    'riotgames',
    'roblox',
    'skype',
    'spotify',
    'steam',
    'tiktok',
    'twitch',
    'twitter',
    'xbox',
    'youtube',
    'domain',
]


class APIConnectedAccountResponse(TypedDict):
    id: str
    name: NotRequired[Union[str, None]]
    type: 'discord_typings.APIConnectedAccountProviders'
    friend_sync: bool
    integrations: NotRequired[Union[list['discord_typings.APIConnectedAccountIntegrationResponse'], None]]
    show_activity: bool
    two_way_link: bool
    verified: bool
    visibility: 'discord_typings.APIConnectedAccountVisibility'
    revoked: NotRequired[Union[bool, None]]


APIConnectedAccountVisibility = Literal[
    0,
    1,
]


class APICreateEntitlementRequestData(TypedDict):
    sku_id: 'discord_typings.APISnowflake'
    owner_id: 'discord_typings.APISnowflake'
    owner_type: 'discord_typings.APIEntitlementOwnerTypes'


class APICreateForumThreadRequest(TypedDict):
    name: str
    auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    rate_limit_per_user: NotRequired[Union[int, None]]
    applied_tags: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    message: 'discord_typings.APIBaseCreateMessageCreateRequest'


class APICreateGroupDMInviteRequest(TypedDict):
    max_age: NotRequired[Union[int, None]]


class APICreateGuildChannelRequest(TypedDict):
    type: NotRequired[Union[None, Literal[0, 2, 4, 5, 13, 14, 15]]]
    name: str
    position: NotRequired[Union[int, None]]
    topic: NotRequired[Union[str, None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    nsfw: NotRequired[Union[bool, None]]
    rate_limit_per_user: NotRequired[Union[int, None]]
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    permission_overwrites: NotRequired[Union[list['discord_typings.APIChannelPermissionOverwriteRequest'], None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]
    default_auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    default_reaction_emoji: NotRequired[Union[None, 'discord_typings.APIUpdateDefaultReactionEmojiRequest']]
    default_thread_rate_limit_per_user: NotRequired[Union[int, None]]
    default_sort_order: NotRequired[Union[None, 'discord_typings.APIThreadSortOrder']]
    default_forum_layout: NotRequired[Union[None, 'discord_typings.APIForumLayout']]
    available_tags: NotRequired[Union[list[Union[None, 'discord_typings.APICreateOrUpdateThreadTagRequest']], None]]


class APICreateGuildInviteRequest(TypedDict):
    max_age: NotRequired[Union[int, None]]
    temporary: NotRequired[Union[bool, None]]
    max_uses: NotRequired[Union[int, None]]
    unique: NotRequired[Union[bool, None]]
    target_user_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    target_application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    target_type: NotRequired[Union[None, Literal[1, 2]]]


class APICreateGuildRequestChannelItem(TypedDict):
    type: NotRequired[Union[None, Literal[0, 2, 4]]]
    name: str
    position: NotRequired[Union[int, None]]
    topic: NotRequired[Union[str, None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    nsfw: NotRequired[Union[bool, None]]
    rate_limit_per_user: NotRequired[Union[int, None]]
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    permission_overwrites: NotRequired[Union[list['discord_typings.APIChannelPermissionOverwriteRequest'], None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]
    default_auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    default_reaction_emoji: NotRequired[Union[None, 'discord_typings.APIUpdateDefaultReactionEmojiRequest']]
    default_thread_rate_limit_per_user: NotRequired[Union[int, None]]
    default_sort_order: NotRequired[Union[None, 'discord_typings.APIThreadSortOrder']]
    default_forum_layout: NotRequired[Union[None, 'discord_typings.APIForumLayout']]
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    available_tags: NotRequired[Union[list['discord_typings.APICreateOrUpdateThreadTagRequest'], None]]


class APICreateGuildRequestRoleItem(TypedDict):
    id: int
    name: NotRequired[Union[str, None]]
    permissions: NotRequired[Union[int, None]]
    color: NotRequired[Union[int, None]]
    hoist: NotRequired[Union[bool, None]]
    mentionable: NotRequired[Union[bool, None]]
    unicode_emoji: NotRequired[Union[str, None]]


class APICreateMessageInteractionCallbackRequest(TypedDict):
    type: Literal[4, 5]
    data: NotRequired[Union[None, 'discord_typings.APIIncomingWebhookInteractionRequest']]


class APICreateMessageInteractionCallbackResponse(TypedDict):
    type: Literal[4]
    message: 'discord_typings.APIMessageResponse'


class APICreateOrUpdateThreadTagRequest(TypedDict):
    name: str
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]
    moderated: NotRequired[Union[bool, None]]


class APICreatePrivateChannelRequest(TypedDict):
    recipient_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    access_tokens: NotRequired[Union[list[str], None]]
    nicks: NotRequired[Union[dict[str, Union[str, None]], None]]


class APICreateTextThreadWithMessageRequest(TypedDict):
    name: str
    auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    rate_limit_per_user: NotRequired[Union[int, None]]


class APICreateTextThreadWithoutMessageRequest(TypedDict):
    name: str
    auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    rate_limit_per_user: NotRequired[Union[int, None]]
    type: NotRequired[Union[None, Literal[10, 11, 12]]]
    invitable: NotRequired[Union[bool, None]]


class APICreatedThreadResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[10, 11, 12]
    last_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    flags: int
    last_pin_timestamp: NotRequired[Union[str, None]]
    guild_id: 'discord_typings.APISnowflake'
    name: str
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    rate_limit_per_user: NotRequired[Union[int, None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]
    permissions: NotRequired[Union[str, None]]
    owner_id: 'discord_typings.APISnowflake'
    thread_metadata: NotRequired[Union[None, 'discord_typings.APIThreadMetadataResponse']]
    message_count: int
    member_count: int
    total_message_sent: int
    applied_tags: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    member: NotRequired[Union[None, 'discord_typings.APIThreadMemberResponse']]


class APIDefaultKeywordListTriggerMetadata(TypedDict):
    allow_list: NotRequired[Union[list[str], None]]
    presets: NotRequired[Union[list['discord_typings.APIAutomodKeywordPresetType'], None]]


class APIDefaultKeywordListTriggerMetadataResponse(TypedDict):
    allow_list: list[str]
    presets: list['discord_typings.APIAutomodKeywordPresetType']


class APIDefaultKeywordListUpsertRequest(TypedDict):
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: Literal[4]
    trigger_metadata: 'discord_typings.APIDefaultKeywordListTriggerMetadata'


class APIDefaultKeywordListUpsertRequestPartial(TypedDict):
    name: NotRequired[str]
    event_type: NotRequired['discord_typings.APIAutomodEventType']
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: NotRequired[Literal[4]]
    trigger_metadata: NotRequired['discord_typings.APIDefaultKeywordListTriggerMetadata']


class APIDefaultKeywordRuleResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    creator_id: 'discord_typings.APISnowflake'
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: list[Union['discord_typings.APIBlockMessageActionResponse', 'discord_typings.APIFlagToChannelActionResponse', 'discord_typings.APIQuarantineUserActionResponse', 'discord_typings.APIUserCommunicationDisabledActionResponse']]
    trigger_type: Literal[4]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_metadata: 'discord_typings.APIDefaultKeywordListTriggerMetadataResponse'


class APIDefaultReactionEmojiResponse(TypedDict):
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]


class APIDiscordIntegrationResponse(TypedDict):
    type: Literal['discord']
    name: NotRequired[Union[str, None]]
    account: NotRequired[Union[None, 'discord_typings.APIAccountResponse']]
    enabled: NotRequired[Union[bool, None]]
    id: 'discord_typings.APISnowflake'
    application: 'discord_typings.APIIntegrationApplicationResponse'
    scopes: list[Literal['applications.commands', 'bot', 'webhook.incoming']]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


class APIEmbeddedActivityInstance(TypedDict):
    application_id: 'discord_typings.APISnowflake'
    instance_id: str
    launch_id: str
    location: NotRequired[Union['discord_typings.APIGuildChannelLocation', 'discord_typings.APIPrivateChannelLocation', None]]
    users: list['discord_typings.APISnowflake']


APIEmbeddedActivityLocationKind = Literal[
    'gc',
    'pc',
]


class APIEmojiResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    roles: list['discord_typings.APISnowflake']
    require_colons: bool
    managed: bool
    animated: bool
    available: bool


APIEntitlementOwnerTypes = Literal[
]


class APIEntitlementResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    sku_id: 'discord_typings.APISnowflake'
    application_id: 'discord_typings.APISnowflake'
    user_id: 'discord_typings.APISnowflake'
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    deleted: bool
    starts_at: NotRequired[Union[str, None]]
    ends_at: NotRequired[Union[str, None]]
    type: 'discord_typings.APIEntitlementTypes'
    fulfilled_at: NotRequired[Union[str, None]]
    fulfillment_status: NotRequired[Union[None, 'discord_typings.APIEntitlementTenantFulfillmentStatusResponse']]
    consumed: NotRequired[Union[bool, None]]


APIEntitlementTenantFulfillmentStatusResponse = Literal[
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]


APIEntitlementTypes = Literal[
    8,
    10,
]


class APIEntityMetadataExternal(TypedDict):
    location: str


class APIEntityMetadataExternalResponse(TypedDict):
    location: str


class APIEntityMetadataStageInstance(TypedDict):
    pass


class APIEntityMetadataStageInstanceResponse(TypedDict):
    pass


class APIEntityMetadataVoice(TypedDict):
    pass


class APIEntityMetadataVoiceResponse(TypedDict):
    pass


class APIExternalConnectionIntegrationResponse(TypedDict):
    type: Literal['twitch', 'youtube']
    name: NotRequired[Union[str, None]]
    account: NotRequired[Union[None, 'discord_typings.APIAccountResponse']]
    enabled: NotRequired[Union[bool, None]]
    id: str
    user: 'discord_typings.APIUserResponse'
    revoked: NotRequired[Union[bool, None]]
    expire_behavior: NotRequired[Union[None, 'discord_typings.APIIntegrationExpireBehaviorTypes']]
    expire_grace_period: NotRequired[Union[None, 'discord_typings.APIIntegrationExpireGracePeriodTypes']]
    subscriber_count: NotRequired[Union[int, None]]
    synced_at: NotRequired[Union[str, None]]
    role_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    syncing: NotRequired[Union[bool, None]]
    enable_emoticons: NotRequired[Union[bool, None]]


class APIExternalScheduledEventCreateRequest(TypedDict):
    name: str
    description: NotRequired[Union[str, None]]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    entity_type: Literal[3]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    entity_metadata: 'discord_typings.APIEntityMetadataExternal'


class APIExternalScheduledEventPatchRequestPartial(TypedDict):
    status: NotRequired[Union[None, 'discord_typings.APIGuildScheduledEventStatuses']]
    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: NotRequired[str]
    scheduled_end_time: NotRequired[Union[str, None]]
    entity_type: NotRequired[Union[None, Literal[3]]]
    privacy_level: NotRequired['discord_typings.APIGuildScheduledEventPrivacyLevels']
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    entity_metadata: NotRequired['discord_typings.APIEntityMetadataExternal']


class APIExternalScheduledEventResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    name: str
    description: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    status: 'discord_typings.APIGuildScheduledEventStatuses'
    entity_type: Literal[3]
    entity_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    user_count: NotRequired[Union[int, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    user_rsvp: NotRequired[Union[None, 'discord_typings.APIScheduledEventUserResponse']]
    entity_metadata: 'discord_typings.APIEntityMetadataExternalResponse'


class APIFlagToChannelAction(TypedDict):
    type: Literal[2]
    metadata: 'discord_typings.APIFlagToChannelActionMetadata'


class APIFlagToChannelActionMetadata(TypedDict):
    channel_id: 'discord_typings.APISnowflake'


class APIFlagToChannelActionMetadataResponse(TypedDict):
    channel_id: 'discord_typings.APISnowflake'


class APIFlagToChannelActionResponse(TypedDict):
    type: Literal[2]
    metadata: 'discord_typings.APIFlagToChannelActionMetadataResponse'


APIForumLayout = Literal[
    0,
    1,
    2,
]


class APIForumTagResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    moderated: bool
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]


class APIFriendInviteResponse(TypedDict):
    type: NotRequired[Union[None, Literal[2]]]
    code: str
    inviter: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    max_age: NotRequired[Union[int, None]]
    created_at: NotRequired[Union[str, None]]
    expires_at: NotRequired[Union[str, None]]
    friends_count: NotRequired[Union[int, None]]
    channel: NotRequired[Union[None, 'discord_typings.APIInviteChannelResponse']]
    is_contact: NotRequired[Union[bool, None]]
    uses: NotRequired[Union[int, None]]
    max_uses: NotRequired[Union[int, None]]
    flags: NotRequired[Union[int, None]]


class APIGatewayBotResponse(TypedDict):
    url: str
    session_start_limit: 'discord_typings.APIGatewayBotSessionStartLimitResponse'
    shards: int


class APIGatewayBotSessionStartLimitResponse(TypedDict):
    max_concurrency: int
    remaining: int
    reset_after: int
    total: int


class APIGatewayResponse(TypedDict):
    url: str


class APIGithubAuthor(TypedDict):
    username: NotRequired[Union[str, None]]
    name: str


class APIGithubCheckApp(TypedDict):
    name: str


class APIGithubCheckPullRequest(TypedDict):
    number: int


class APIGithubCheckRun(TypedDict):
    conclusion: NotRequired[Union[str, None]]
    name: str
    html_url: str
    check_suite: 'discord_typings.APIGithubCheckSuite'
    details_url: NotRequired[Union[str, None]]
    output: NotRequired[Union[None, 'discord_typings.APIGithubCheckRunOutput']]
    pull_requests: NotRequired[Union[list['discord_typings.APIGithubCheckPullRequest'], None]]


class APIGithubCheckRunOutput(TypedDict):
    title: NotRequired[Union[str, None]]
    summary: NotRequired[Union[str, None]]


class APIGithubCheckSuite(TypedDict):
    conclusion: NotRequired[Union[str, None]]
    head_branch: NotRequired[Union[str, None]]
    head_sha: str
    pull_requests: NotRequired[Union[list['discord_typings.APIGithubCheckPullRequest'], None]]
    app: 'discord_typings.APIGithubCheckApp'


class APIGithubComment(TypedDict):
    id: int
    html_url: str
    user: 'discord_typings.APIGithubUser'
    commit_id: NotRequired[Union[str, None]]
    body: str


class APIGithubCommit(TypedDict):
    id: str
    url: str
    message: str
    author: 'discord_typings.APIGithubAuthor'


class APIGithubDiscussion(TypedDict):
    title: str
    number: int
    html_url: str
    answer_html_url: NotRequired[Union[str, None]]
    body: NotRequired[Union[str, None]]
    user: 'discord_typings.APIGithubUser'


class APIGithubIssue(TypedDict):
    id: int
    number: int
    html_url: str
    user: 'discord_typings.APIGithubUser'
    title: str
    body: NotRequired[Union[str, None]]
    pull_request: NotRequired[Any]


class APIGithubRelease(TypedDict):
    id: int
    tag_name: str
    html_url: str
    author: 'discord_typings.APIGithubUser'


class APIGithubRepository(TypedDict):
    id: int
    html_url: str
    name: str
    full_name: str


class APIGithubReview(TypedDict):
    user: 'discord_typings.APIGithubUser'
    body: NotRequired[Union[str, None]]
    html_url: str
    state: str


class APIGithubUser(TypedDict):
    id: int
    login: str
    html_url: str
    avatar_url: str


class APIGithubWebhook(TypedDict):
    action: NotRequired[Union[str, None]]
    ref: NotRequired[Union[str, None]]
    ref_type: NotRequired[Union[str, None]]
    comment: NotRequired[Union[None, 'discord_typings.APIGithubComment']]
    issue: NotRequired[Union[None, 'discord_typings.APIGithubIssue']]
    pull_request: NotRequired[Union[None, 'discord_typings.APIGithubIssue']]
    repository: NotRequired[Union[None, 'discord_typings.APIGithubRepository']]
    forkee: NotRequired[Union[None, 'discord_typings.APIGithubRepository']]
    sender: 'discord_typings.APIGithubUser'
    member: NotRequired[Union[None, 'discord_typings.APIGithubUser']]
    release: NotRequired[Union[None, 'discord_typings.APIGithubRelease']]
    head_commit: NotRequired[Union[None, 'discord_typings.APIGithubCommit']]
    commits: NotRequired[Union[list['discord_typings.APIGithubCommit'], None]]
    forced: NotRequired[Union[bool, None]]
    compare: NotRequired[Union[str, None]]
    review: NotRequired[Union[None, 'discord_typings.APIGithubReview']]
    check_run: NotRequired[Union[None, 'discord_typings.APIGithubCheckRun']]
    check_suite: NotRequired[Union[None, 'discord_typings.APIGithubCheckSuite']]
    discussion: NotRequired[Union[None, 'discord_typings.APIGithubDiscussion']]
    answer: NotRequired[Union[None, 'discord_typings.APIGithubComment']]


class APIGroupDMInviteResponse(TypedDict):
    type: NotRequired[Union[None, Literal[1]]]
    code: str
    inviter: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    max_age: NotRequired[Union[int, None]]
    created_at: NotRequired[Union[str, None]]
    expires_at: NotRequired[Union[str, None]]
    channel: NotRequired[Union[None, 'discord_typings.APIInviteChannelResponse']]
    approximate_member_count: NotRequired[Union[int, None]]


class APIGuildAuditLogResponse(TypedDict):
    audit_log_entries: list['discord_typings.APIAuditLogEntryResponse']
    users: list['discord_typings.APIUserResponse']
    integrations: list[Union['discord_typings.APIPartialDiscordIntegrationResponse', 'discord_typings.APIPartialExternalConnectionIntegrationResponse', 'discord_typings.APIPartialGuildSubscriptionIntegrationResponse']]
    webhooks: list[Union['discord_typings.APIApplicationIncomingWebhookResponse', 'discord_typings.APIChannelFollowerWebhookResponse', 'discord_typings.APIGuildIncomingWebhookResponse']]
    guild_scheduled_events: list[Union['discord_typings.APIExternalScheduledEventResponse', 'discord_typings.APIStageScheduledEventResponse', 'discord_typings.APIVoiceScheduledEventResponse']]
    threads: list['discord_typings.APIThreadResponse']
    application_commands: list['discord_typings.APIApplicationCommandResponse']
    auto_moderation_rules: list[Union['discord_typings.APIDefaultKeywordRuleResponse', 'discord_typings.APIKeywordRuleResponse', 'discord_typings.APIMLSpamRuleResponse', 'discord_typings.APIMentionSpamRuleResponse', 'discord_typings.APISpamLinkRuleResponse', None]]


class APIGuildBanResponse(TypedDict):
    user: 'discord_typings.APIUserResponse'
    reason: NotRequired[Union[str, None]]


class APIGuildChannelLocation(TypedDict):
    id: str
    kind: Literal['gc']
    channel_id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'


class APIGuildChannelResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[0, 2, 4, 5, 13, 14, 15]
    last_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    flags: int
    last_pin_timestamp: NotRequired[Union[str, None]]
    guild_id: 'discord_typings.APISnowflake'
    name: str
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    rate_limit_per_user: NotRequired[Union[int, None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]
    permissions: NotRequired[Union[str, None]]
    topic: NotRequired[Union[str, None]]
    default_auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    default_thread_rate_limit_per_user: NotRequired[Union[int, None]]
    position: int
    permission_overwrites: NotRequired[Union[list['discord_typings.APIChannelPermissionOverwriteResponse'], None]]
    nsfw: NotRequired[Union[bool, None]]
    available_tags: NotRequired[Union[list['discord_typings.APIForumTagResponse'], None]]
    default_reaction_emoji: NotRequired[Union[None, 'discord_typings.APIDefaultReactionEmojiResponse']]
    default_sort_order: NotRequired[Union[None, 'discord_typings.APIThreadSortOrder']]
    default_forum_layout: NotRequired[Union[None, 'discord_typings.APIForumLayout']]
    hd_streaming_until: NotRequired[Union[str, None]]
    hd_streaming_buyer_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIGuildCreateRequest(TypedDict):
    description: NotRequired[Union[str, None]]
    name: str
    region: NotRequired[Union[str, None]]
    icon: NotRequired[Union[str, None]]
    verification_level: NotRequired[Union[None, 'discord_typings.APIVerificationLevels']]
    default_message_notifications: NotRequired[Union[None, 'discord_typings.APIUserNotificationSettings']]
    explicit_content_filter: NotRequired[Union[None, 'discord_typings.APIGuildExplicitContentFilterTypes']]
    preferred_locale: NotRequired[Union[None, 'discord_typings.APIAvailableLocalesEnum']]
    afk_timeout: NotRequired[Union[None, 'discord_typings.APIAfkTimeouts']]
    roles: NotRequired[Union[list['discord_typings.APICreateGuildRequestRoleItem'], None]]
    channels: NotRequired[Union[list['discord_typings.APICreateGuildRequestChannelItem'], None]]
    afk_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    system_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    system_channel_flags: NotRequired[Union[int, None]]


APIGuildExplicitContentFilterTypes = Literal[
    0,
    1,
    2,
]


APIGuildFeatures = Literal[
    'ANIMATED_BANNER',
    'ANIMATED_ICON',
    'APPLICATION_COMMAND_PERMISSIONS_V2',
    'AUTO_MODERATION',
    'BANNER',
    'COMMUNITY',
    'CREATOR_MONETIZABLE_PROVISIONAL',
    'CREATOR_STORE_PAGE',
    'DEVELOPER_SUPPORT_SERVER',
    'DISCOVERABLE',
    'FEATURABLE',
    'INVITES_DISABLED',
    'INVITE_SPLASH',
    'MEMBER_VERIFICATION_GATE_ENABLED',
    'MORE_STICKERS',
    'NEWS',
    'PARTNERED',
    'PREVIEW_ENABLED',
    'RAID_ALERTS_DISABLED',
    'ROLE_ICONS',
    'ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE',
    'ROLE_SUBSCRIPTIONS_ENABLED',
    'TICKETED_EVENTS_ENABLED',
    'VANITY_URL',
    'VERIFIED',
    'VIP_REGIONS',
    'WELCOME_SCREEN_ENABLED',
]


class APIGuildHomeSettingsResponse(TypedDict):
    guild_id: 'discord_typings.APISnowflake'
    enabled: bool
    welcome_message: NotRequired[Union[None, 'discord_typings.APIWelcomeMessageResponse']]
    new_member_actions: NotRequired[Union[list[Union[None, 'discord_typings.APINewMemberActionResponse']], None]]
    resource_channels: NotRequired[Union[list[Union[None, 'discord_typings.APIResourceChannelResponse']], None]]


class APIGuildIncomingWebhookResponse(TypedDict):
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    avatar: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    id: 'discord_typings.APISnowflake'
    name: str
    type: Literal[1]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    token: NotRequired[Union[str, None]]
    url: NotRequired[Union[str, None]]


class APIGuildInviteResponse(TypedDict):
    type: NotRequired[Union[None, Literal[0]]]
    code: str
    inviter: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    max_age: NotRequired[Union[int, None]]
    created_at: NotRequired[Union[str, None]]
    expires_at: NotRequired[Union[str, None]]
    is_contact: NotRequired[Union[bool, None]]
    flags: NotRequired[Union[int, None]]
    guild: NotRequired[Union[None, 'discord_typings.APIInviteGuildResponse']]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    channel: NotRequired[Union[None, 'discord_typings.APIInviteChannelResponse']]
    stage_instance: NotRequired[Union[None, 'discord_typings.APIInviteStageInstanceResponse']]
    target_type: NotRequired[Union[None, 'discord_typings.APIInviteTargetTypes']]
    target_user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    target_application: NotRequired[Union[None, 'discord_typings.APIInviteApplicationResponse']]
    guild_scheduled_event: NotRequired[Union[None, 'discord_typings.APIScheduledEventResponse']]
    uses: NotRequired[Union[int, None]]
    max_uses: NotRequired[Union[int, None]]
    temporary: NotRequired[Union[bool, None]]
    approximate_member_count: NotRequired[Union[int, None]]
    approximate_presence_count: NotRequired[Union[int, None]]
    is_nickname_changeable: NotRequired[Union[bool, None]]


APIGuildMFALevel = Literal[
    0,
    1,
]


class APIGuildMFALevelResponse(TypedDict):
    level: 'discord_typings.APIGuildMFALevel'


class APIGuildMemberResponse(TypedDict):
    avatar: NotRequired[Union[str, None]]
    avatar_decoration_data: NotRequired[Union[None, 'discord_typings.APIUserAvatarDecorationResponse']]
    banner: NotRequired[Union[str, None]]
    communication_disabled_until: NotRequired[Union[str, None]]
    flags: int
    joined_at: str
    nick: NotRequired[Union[str, None]]
    pending: bool
    premium_since: NotRequired[Union[str, None]]
    roles: list['discord_typings.APISnowflake']
    user: 'discord_typings.APIUserResponse'
    mute: bool
    deaf: bool


APIGuildNSFWContentLevel = Literal[
    0,
    1,
    2,
    3,
]


APIGuildOnboardingMode = Literal[
    0,
    1,
]


class APIGuildOnboardingResponse(TypedDict):
    guild_id: 'discord_typings.APISnowflake'
    prompts: list['discord_typings.APIOnboardingPromptResponse']
    default_channel_ids: list['discord_typings.APISnowflake']
    enabled: bool


class APIGuildPatchRequestPartial(TypedDict):
    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    region: NotRequired[Union[str, None]]
    icon: NotRequired[Union[str, None]]
    verification_level: NotRequired[Union[None, 'discord_typings.APIVerificationLevels']]
    default_message_notifications: NotRequired[Union[None, 'discord_typings.APIUserNotificationSettings']]
    explicit_content_filter: NotRequired[Union[None, 'discord_typings.APIGuildExplicitContentFilterTypes']]
    preferred_locale: NotRequired[Union[None, 'discord_typings.APIAvailableLocalesEnum']]
    afk_timeout: NotRequired[Union[None, 'discord_typings.APIAfkTimeouts']]
    afk_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    system_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    owner_id: NotRequired['discord_typings.APISnowflake']
    splash: NotRequired[Union[str, None]]
    banner: NotRequired[Union[str, None]]
    system_channel_flags: NotRequired[Union[int, None]]
    features: NotRequired[Union[list[Union[str, None]], None]]
    discovery_splash: NotRequired[Union[str, None]]
    home_header: NotRequired[Union[str, None]]
    rules_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    safety_alerts_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    public_updates_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    premium_progress_bar_enabled: NotRequired[Union[bool, None]]


class APIGuildPreviewResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    home_header: NotRequired[Union[str, None]]
    splash: NotRequired[Union[str, None]]
    discovery_splash: NotRequired[Union[str, None]]
    features: list['discord_typings.APIGuildFeatures']
    approximate_member_count: int
    approximate_presence_count: int
    emojis: list['discord_typings.APIEmojiResponse']
    stickers: list['discord_typings.APIGuildStickerResponse']


class APIGuildProductPurchaseResponse(TypedDict):
    listing_id: 'discord_typings.APISnowflake'
    product_name: str


class APIGuildPruneResponse(TypedDict):
    pruned: NotRequired[Union[int, None]]


class APIGuildResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    home_header: NotRequired[Union[str, None]]
    splash: NotRequired[Union[str, None]]
    discovery_splash: NotRequired[Union[str, None]]
    features: list['discord_typings.APIGuildFeatures']
    banner: NotRequired[Union[str, None]]
    owner_id: 'discord_typings.APISnowflake'
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    region: str
    afk_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    afk_timeout: 'discord_typings.APIAfkTimeouts'
    system_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    system_channel_flags: int
    widget_enabled: bool
    widget_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    verification_level: 'discord_typings.APIVerificationLevels'
    roles: list['discord_typings.APIGuildRoleResponse']
    default_message_notifications: 'discord_typings.APIUserNotificationSettings'
    mfa_level: 'discord_typings.APIGuildMFALevel'
    explicit_content_filter: 'discord_typings.APIGuildExplicitContentFilterTypes'
    max_presences: NotRequired[Union[int, None]]
    max_members: NotRequired[Union[int, None]]
    max_stage_video_channel_users: NotRequired[Union[int, None]]
    max_video_channel_users: NotRequired[Union[int, None]]
    vanity_url_code: NotRequired[Union[str, None]]
    premium_tier: 'discord_typings.APIPremiumGuildTiers'
    premium_subscription_count: int
    preferred_locale: 'discord_typings.APIAvailableLocalesEnum'
    rules_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    safety_alerts_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    public_updates_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    premium_progress_bar_enabled: bool
    nsfw: bool
    nsfw_level: 'discord_typings.APIGuildNSFWContentLevel'
    emojis: list['discord_typings.APIEmojiResponse']
    stickers: list['discord_typings.APIGuildStickerResponse']


class APIGuildRoleResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    description: NotRequired[Union[str, None]]
    permissions: str
    position: int
    color: int
    hoist: bool
    managed: bool
    mentionable: bool
    icon: NotRequired[Union[str, None]]
    unicode_emoji: NotRequired[Union[str, None]]
    tags: NotRequired[Union[None, 'discord_typings.APIGuildRoleTagsResponse']]


class APIGuildRoleTagsResponse(TypedDict):
    premium_subscriber: NotRequired[None]
    bot_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    integration_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    subscription_listing_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    available_for_purchase: NotRequired[None]
    guild_connections: NotRequired[None]


APIGuildScheduledEventEntityTypes = Literal[
    0,
    1,
    2,
    3,
]


APIGuildScheduledEventPrivacyLevels = Literal[
    2,
]


APIGuildScheduledEventStatuses = Literal[
    1,
    2,
    3,
    4,
]


class APIGuildStickerResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    tags: str
    type: Literal[2]
    format_type: NotRequired[Union[None, 'discord_typings.APIStickerFormatTypes']]
    description: NotRequired[Union[str, None]]
    available: bool
    guild_id: 'discord_typings.APISnowflake'
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


class APIGuildSubscriptionIntegrationResponse(TypedDict):
    type: Literal['guild_subscription']
    name: NotRequired[Union[str, None]]
    account: NotRequired[Union[None, 'discord_typings.APIAccountResponse']]
    enabled: NotRequired[Union[bool, None]]
    id: 'discord_typings.APISnowflake'


class APIGuildTemplateChannelResponse(TypedDict):
    id: NotRequired[Union[int, None]]
    type: Literal[0, 2, 4]
    name: NotRequired[Union[str, None]]
    position: NotRequired[Union[int, None]]
    topic: NotRequired[Union[str, None]]
    bitrate: int
    user_limit: int
    nsfw: bool
    rate_limit_per_user: int
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    default_auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    permission_overwrites: list[Union[None, 'discord_typings.APIChannelPermissionOverwriteResponse']]
    available_tags: NotRequired[Union[list['discord_typings.APIGuildTemplateChannelTags'], None]]
    template: str
    default_reaction_emoji: NotRequired[Union[None, 'discord_typings.APIDefaultReactionEmojiResponse']]
    default_thread_rate_limit_per_user: NotRequired[Union[int, None]]
    default_sort_order: NotRequired[Union[None, 'discord_typings.APIThreadSortOrder']]
    default_forum_layout: NotRequired[Union[None, 'discord_typings.APIForumLayout']]
    icon_emoji: NotRequired[Union[None, 'discord_typings.APIIconEmojiResponse']]
    theme_color: NotRequired[Union[int, None]]


class APIGuildTemplateChannelTags(TypedDict):
    name: str
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]
    moderated: NotRequired[Union[bool, None]]


class APIGuildTemplateResponse(TypedDict):
    code: str
    name: str
    description: NotRequired[Union[str, None]]
    usage_count: int
    creator_id: 'discord_typings.APISnowflake'
    creator: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    created_at: str
    updated_at: str
    source_guild_id: 'discord_typings.APISnowflake'
    serialized_source_guild: 'discord_typings.APIGuildTemplateSnapshotResponse'
    is_dirty: NotRequired[Union[bool, None]]


class APIGuildTemplateRoleResponse(TypedDict):
    id: int
    name: str
    permissions: str
    color: int
    hoist: bool
    mentionable: bool
    icon: NotRequired[Union[str, None]]
    unicode_emoji: NotRequired[Union[str, None]]


class APIGuildTemplateSnapshotResponse(TypedDict):
    name: str
    description: NotRequired[Union[str, None]]
    region: NotRequired[Union[str, None]]
    verification_level: 'discord_typings.APIVerificationLevels'
    default_message_notifications: 'discord_typings.APIUserNotificationSettings'
    explicit_content_filter: 'discord_typings.APIGuildExplicitContentFilterTypes'
    preferred_locale: 'discord_typings.APIAvailableLocalesEnum'
    afk_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    afk_timeout: 'discord_typings.APIAfkTimeouts'
    system_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    system_channel_flags: int
    roles: list['discord_typings.APIGuildTemplateRoleResponse']
    channels: list['discord_typings.APIGuildTemplateChannelResponse']


class APIGuildWelcomeChannel(TypedDict):
    channel_id: 'discord_typings.APISnowflake'
    description: str
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]


class APIGuildWelcomeScreenChannelResponse(TypedDict):
    channel_id: 'discord_typings.APISnowflake'
    description: str
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]


class APIGuildWelcomeScreenResponse(TypedDict):
    description: NotRequired[Union[str, None]]
    welcome_channels: list['discord_typings.APIGuildWelcomeScreenChannelResponse']


class APIGuildWithCountsResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    home_header: NotRequired[Union[str, None]]
    splash: NotRequired[Union[str, None]]
    discovery_splash: NotRequired[Union[str, None]]
    features: list['discord_typings.APIGuildFeatures']
    banner: NotRequired[Union[str, None]]
    owner_id: 'discord_typings.APISnowflake'
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    region: str
    afk_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    afk_timeout: 'discord_typings.APIAfkTimeouts'
    system_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    system_channel_flags: int
    widget_enabled: bool
    widget_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    verification_level: 'discord_typings.APIVerificationLevels'
    roles: list['discord_typings.APIGuildRoleResponse']
    default_message_notifications: 'discord_typings.APIUserNotificationSettings'
    mfa_level: 'discord_typings.APIGuildMFALevel'
    explicit_content_filter: 'discord_typings.APIGuildExplicitContentFilterTypes'
    max_presences: NotRequired[Union[int, None]]
    max_members: NotRequired[Union[int, None]]
    max_stage_video_channel_users: NotRequired[Union[int, None]]
    max_video_channel_users: NotRequired[Union[int, None]]
    vanity_url_code: NotRequired[Union[str, None]]
    premium_tier: 'discord_typings.APIPremiumGuildTiers'
    premium_subscription_count: int
    preferred_locale: 'discord_typings.APIAvailableLocalesEnum'
    rules_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    safety_alerts_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    public_updates_channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    premium_progress_bar_enabled: bool
    nsfw: bool
    nsfw_level: 'discord_typings.APIGuildNSFWContentLevel'
    emojis: list['discord_typings.APIEmojiResponse']
    stickers: list['discord_typings.APIGuildStickerResponse']
    approximate_member_count: NotRequired[Union[int, None]]
    approximate_presence_count: NotRequired[Union[int, None]]


class APIIconEmojiResponse(TypedDict):
    pass


class APIIncomingWebhookInteractionRequest(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollCreateRequest']]
    tts: NotRequired[Union[bool, None]]
    flags: NotRequired[Union[int, None]]


class APIIncomingWebhookRequestPartial(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollCreateRequest']]
    tts: NotRequired[Union[bool, None]]
    flags: NotRequired[Union[int, None]]
    username: NotRequired[Union[str, None]]
    avatar_url: NotRequired[Union[str, None]]
    thread_name: NotRequired[Union[str, None]]
    applied_tags: NotRequired[Union[list['discord_typings.APISnowflake'], None]]


class APIIncomingWebhookUpdateForInteractionCallbackRequestPartial(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    flags: NotRequired[Union[int, None]]


class APIIncomingWebhookUpdateRequestPartial(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollCreateRequest']]
    flags: NotRequired[Union[int, None]]


class APIIntegrationApplicationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: str
    type: NotRequired[Union[None, 'discord_typings.APIApplicationTypes']]
    cover_image: NotRequired[Union[str, None]]
    primary_sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    bot: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


APIIntegrationExpireBehaviorTypes = Literal[
    0,
    1,
]


APIIntegrationExpireGracePeriodTypes = Literal[
    1,
    3,
    7,
    14,
    30,
]


APIIntegrationTypes = Literal[
    'discord',
    'twitch',
    'youtube',
    'guild_subscription',
]


class APIInteractionApplicationCommandAutocompleteCallbackIntegerData(TypedDict):
    choices: NotRequired[Union[list[Union[None, 'discord_typings.APIApplicationCommandOptionIntegerChoice']], None]]


class APIInteractionApplicationCommandAutocompleteCallbackNumberData(TypedDict):
    choices: NotRequired[Union[list[Union[None, 'discord_typings.APIApplicationCommandOptionNumberChoice']], None]]


class APIInteractionApplicationCommandAutocompleteCallbackStringData(TypedDict):
    choices: NotRequired[Union[list[Union[None, 'discord_typings.APIApplicationCommandOptionStringChoice']], None]]


class APIInteractionCallbackResponse(TypedDict):
    interaction: 'discord_typings.APIInteractionResponse'
    resource: NotRequired[Union['discord_typings.APICreateMessageInteractionCallbackResponse', 'discord_typings.APILaunchActivityInteractionCallbackResponse', 'discord_typings.APIUpdateMessageInteractionCallbackResponse', None]]


APIInteractionCallbackTypes = Literal[
    1,
    4,
    5,
    6,
    7,
    8,
    9,
    12,
]


APIInteractionContextType = Literal[
    0,
    1,
    2,
]


class APIInteractionResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIInteractionTypes'
    response_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    response_message_loading: NotRequired[Union[bool, None]]
    response_message_ephemeral: NotRequired[Union[bool, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


APIInteractionTypes = Literal[
    1,
    2,
    3,
    4,
    5,
]


class APIInviteApplicationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: str
    type: NotRequired[Union[None, 'discord_typings.APIApplicationTypes']]
    cover_image: NotRequired[Union[str, None]]
    primary_sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    bot: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    slug: NotRequired[Union[str, None]]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    rpc_origins: NotRequired[Union[list[Union[str, None]], None]]
    bot_public: NotRequired[Union[bool, None]]
    bot_require_code_grant: NotRequired[Union[bool, None]]
    terms_of_service_url: NotRequired[Union[str, None]]
    privacy_policy_url: NotRequired[Union[str, None]]
    custom_install_url: NotRequired[Union[str, None]]
    install_params: NotRequired[Union[None, 'discord_typings.APIApplicationOAuth2InstallParamsResponse']]
    integration_types_config: NotRequired[Union[dict[str, 'discord_typings.APIApplicationIntegrationTypeConfigurationResponse'], None]]
    verify_key: str
    flags: int
    max_participants: NotRequired[Union[int, None]]
    tags: NotRequired[Union[list[str], None]]


class APIInviteChannelRecipientResponse(TypedDict):
    username: str


class APIInviteChannelResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIChannelTypes'
    name: NotRequired[Union[str, None]]
    icon: NotRequired[Union[str, None]]
    recipients: NotRequired[Union[list['discord_typings.APIInviteChannelRecipientResponse'], None]]


class APIInviteGuildResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    splash: NotRequired[Union[str, None]]
    banner: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    icon: NotRequired[Union[str, None]]
    features: list['discord_typings.APIGuildFeatures']
    verification_level: NotRequired[Union[None, 'discord_typings.APIVerificationLevels']]
    vanity_url_code: NotRequired[Union[str, None]]
    nsfw_level: NotRequired[Union[None, 'discord_typings.APIGuildNSFWContentLevel']]
    nsfw: NotRequired[Union[bool, None]]
    premium_subscription_count: NotRequired[Union[int, None]]


class APIInviteStageInstanceResponse(TypedDict):
    topic: str
    participant_count: NotRequired[Union[int, None]]
    speaker_count: NotRequired[Union[int, None]]
    members: NotRequired[Union[list['discord_typings.APIGuildMemberResponse'], None]]


APIInviteTargetTypes = Literal[
    1,
    2,
    3,
]


APIInviteTypes = Literal[
    0,
    1,
    2,
]


class APIKeywordRuleResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    creator_id: 'discord_typings.APISnowflake'
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: list[Union['discord_typings.APIBlockMessageActionResponse', 'discord_typings.APIFlagToChannelActionResponse', 'discord_typings.APIQuarantineUserActionResponse', 'discord_typings.APIUserCommunicationDisabledActionResponse']]
    trigger_type: Literal[1]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_metadata: 'discord_typings.APIKeywordTriggerMetadataResponse'


class APIKeywordTriggerMetadata(TypedDict):
    keyword_filter: NotRequired[Union[list[str], None]]
    regex_patterns: NotRequired[Union[list[str], None]]
    allow_list: NotRequired[Union[list[str], None]]


class APIKeywordTriggerMetadataResponse(TypedDict):
    keyword_filter: list[str]
    regex_patterns: list[str]
    allow_list: list[str]


class APIKeywordUpsertRequest(TypedDict):
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: Literal[1]
    trigger_metadata: NotRequired[Union[None, 'discord_typings.APIKeywordTriggerMetadata']]


class APIKeywordUpsertRequestPartial(TypedDict):
    name: NotRequired[str]
    event_type: NotRequired['discord_typings.APIAutomodEventType']
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: NotRequired[Literal[1]]
    trigger_metadata: NotRequired[Union[None, 'discord_typings.APIKeywordTriggerMetadata']]


class APILaunchActivityInteractionCallbackRequest(TypedDict):
    type: Literal[12]


class APILaunchActivityInteractionCallbackResponse(TypedDict):
    type: Literal[12]


class APIListApplicationEmojisResponse(TypedDict):
    items: list['discord_typings.APIEmojiResponse']


class APIListGuildSoundboardSoundsResponse(TypedDict):
    items: list['discord_typings.APISoundboardSoundResponse']


class APILobbyMemberRequest(TypedDict):
    id: 'discord_typings.APISnowflake'
    metadata: NotRequired[Union[dict[str, str], None]]
    flags: NotRequired[Union[None, Literal[1]]]


class APILobbyMemberResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    metadata: NotRequired[Union[dict[str, str], None]]
    flags: int


class APILobbyMessageResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIMessageType'
    content: str
    lobby_id: 'discord_typings.APISnowflake'
    channel_id: 'discord_typings.APISnowflake'
    author: 'discord_typings.APIUserResponse'
    metadata: NotRequired[Union[dict[str, str], None]]
    flags: int
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APILobbyResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    application_id: 'discord_typings.APISnowflake'
    metadata: NotRequired[Union[dict[str, str], None]]
    members: NotRequired[Union[list['discord_typings.APILobbyMemberResponse'], None]]
    linked_channel: NotRequired[Union[None, 'discord_typings.APIGuildChannelResponse']]


class APIMLSpamRuleResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    creator_id: 'discord_typings.APISnowflake'
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: list[Union['discord_typings.APIBlockMessageActionResponse', 'discord_typings.APIFlagToChannelActionResponse', 'discord_typings.APIQuarantineUserActionResponse', 'discord_typings.APIUserCommunicationDisabledActionResponse']]
    trigger_type: Literal[3]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_metadata: 'discord_typings.APIMLSpamTriggerMetadataResponse'


class APIMLSpamTriggerMetadata(TypedDict):
    pass


class APIMLSpamTriggerMetadataResponse(TypedDict):
    pass


class APIMLSpamUpsertRequest(TypedDict):
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: Literal[3]
    trigger_metadata: NotRequired[Union[None, 'discord_typings.APIMLSpamTriggerMetadata']]


class APIMLSpamUpsertRequestPartial(TypedDict):
    name: NotRequired[str]
    event_type: NotRequired['discord_typings.APIAutomodEventType']
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: NotRequired[Literal[3]]
    trigger_metadata: NotRequired[Union[None, 'discord_typings.APIMLSpamTriggerMetadata']]


class APIMentionSpamRuleResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    creator_id: 'discord_typings.APISnowflake'
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: list[Union['discord_typings.APIBlockMessageActionResponse', 'discord_typings.APIFlagToChannelActionResponse', 'discord_typings.APIQuarantineUserActionResponse', 'discord_typings.APIUserCommunicationDisabledActionResponse']]
    trigger_type: Literal[5]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_metadata: 'discord_typings.APIMentionSpamTriggerMetadataResponse'


class APIMentionSpamTriggerMetadata(TypedDict):
    mention_total_limit: int
    mention_raid_protection_enabled: NotRequired[Union[bool, None]]


class APIMentionSpamTriggerMetadataResponse(TypedDict):
    mention_total_limit: int
    mention_raid_protection_enabled: NotRequired[Union[bool, None]]


class APIMentionSpamUpsertRequest(TypedDict):
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: Literal[5]
    trigger_metadata: NotRequired[Union[None, 'discord_typings.APIMentionSpamTriggerMetadata']]


class APIMentionSpamUpsertRequestPartial(TypedDict):
    name: NotRequired[str]
    event_type: NotRequired['discord_typings.APIAutomodEventType']
    actions: NotRequired[Union[list[Union['discord_typings.APIBlockMessageAction', 'discord_typings.APIFlagToChannelAction', 'discord_typings.APIQuarantineUserAction', 'discord_typings.APIUserCommunicationDisabledAction']], None]]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_type: NotRequired[Literal[5]]
    trigger_metadata: NotRequired[Union[None, 'discord_typings.APIMentionSpamTriggerMetadata']]


class APIMentionableSelectComponentForMessageRequest(TypedDict):
    type: Literal[7]
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list[Union['discord_typings.APIRoleSelectDefaultValue', 'discord_typings.APIUserSelectDefaultValue']], None]]


class APIMentionableSelectComponentResponse(TypedDict):
    type: Literal[7]
    id: int
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list[Union['discord_typings.APIRoleSelectDefaultValueResponse', 'discord_typings.APIUserSelectDefaultValueResponse']], None]]


class APIMessageActivityResponse(TypedDict):
    pass


class APIMessageAllowedMentionsRequest(TypedDict):
    parse: NotRequired[Union[list[Union[None, 'discord_typings.APIAllowedMentionTypes']], None]]
    users: NotRequired[Union[list[Union[None, 'discord_typings.APISnowflake']], None]]
    roles: NotRequired[Union[list[Union[None, 'discord_typings.APISnowflake']], None]]
    replied_user: NotRequired[Union[bool, None]]


class APIMessageAttachmentRequest(TypedDict):
    id: 'discord_typings.APISnowflake'
    filename: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    duration_secs: NotRequired[Union[float, None]]
    waveform: NotRequired[Union[str, None]]
    title: NotRequired[Union[str, None]]
    is_remix: NotRequired[Union[bool, None]]


class APIMessageAttachmentResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    filename: str
    size: int
    url: str
    proxy_url: str
    width: NotRequired[Union[int, None]]
    height: NotRequired[Union[int, None]]
    duration_secs: NotRequired[Union[float, None]]
    waveform: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    content_type: NotRequired[Union[str, None]]
    ephemeral: NotRequired[Union[bool, None]]
    title: NotRequired[Union[str, None]]
    application: NotRequired[Union[None, 'discord_typings.APIApplicationResponse']]
    clip_created_at: NotRequired[Union[str, None]]
    clip_participants: NotRequired[Union[list['discord_typings.APIUserResponse'], None]]


class APIMessageCallResponse(TypedDict):
    ended_timestamp: NotRequired[Union[str, None]]
    participants: list['discord_typings.APISnowflake']


class APIMessageComponentInteractionMetadataResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[3]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    authorizing_integration_owners: dict[str, 'discord_typings.APISnowflake']
    original_response_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    interacted_message_id: 'discord_typings.APISnowflake'


APIMessageComponentTypes = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]


class APIMessageCreateRequest(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    sticker_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    flags: NotRequired[Union[int, None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollCreateRequest']]
    confetti_potion: NotRequired[Union[None, 'discord_typings.APIConfettiPotionCreateRequest']]
    message_reference: NotRequired[Union[None, 'discord_typings.APIMessageReferenceRequest']]
    nonce: NotRequired[Union[int, str, None]]
    enforce_nonce: NotRequired[Union[bool, None]]
    tts: NotRequired[Union[bool, None]]


class APIMessageEditRequestPartial(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    flags: NotRequired[Union[int, None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    sticker_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]


class APIMessageEmbedAuthorResponse(TypedDict):
    name: str
    url: NotRequired[Union[str, None]]
    icon_url: NotRequired[Union[str, None]]
    proxy_icon_url: NotRequired[Union[str, None]]


class APIMessageEmbedFieldResponse(TypedDict):
    name: str
    value: str
    inline: bool


class APIMessageEmbedFooterResponse(TypedDict):
    text: str
    icon_url: NotRequired[Union[str, None]]
    proxy_icon_url: NotRequired[Union[str, None]]


class APIMessageEmbedImageResponse(TypedDict):
    url: NotRequired[Union[str, None]]
    proxy_url: NotRequired[Union[str, None]]
    width: NotRequired[Union[None, int]]
    height: NotRequired[Union[None, int]]
    placeholder: NotRequired[Union[str, None]]
    placeholder_version: NotRequired[Union[None, int]]
    flags: NotRequired[Union[None, int]]


class APIMessageEmbedProviderResponse(TypedDict):
    name: str
    url: NotRequired[Union[str, None]]


class APIMessageEmbedResponse(TypedDict):
    type: str
    url: NotRequired[Union[str, None]]
    title: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    color: NotRequired[Union[int, None]]
    timestamp: NotRequired[Union[str, None]]
    fields: NotRequired[Union[list['discord_typings.APIMessageEmbedFieldResponse'], None]]
    author: NotRequired[Union[None, 'discord_typings.APIMessageEmbedAuthorResponse']]
    provider: NotRequired[Union[None, 'discord_typings.APIMessageEmbedProviderResponse']]
    image: NotRequired[Union[None, 'discord_typings.APIMessageEmbedImageResponse']]
    thumbnail: NotRequired[Union[None, 'discord_typings.APIMessageEmbedImageResponse']]
    video: NotRequired[Union[None, 'discord_typings.APIMessageEmbedVideoResponse']]
    footer: NotRequired[Union[None, 'discord_typings.APIMessageEmbedFooterResponse']]


class APIMessageEmbedVideoResponse(TypedDict):
    url: NotRequired[Union[str, None]]
    proxy_url: NotRequired[Union[str, None]]
    width: NotRequired[Union[None, int]]
    height: NotRequired[Union[None, int]]
    placeholder: NotRequired[Union[str, None]]
    placeholder_version: NotRequired[Union[None, int]]
    flags: NotRequired[Union[None, int]]


class APIMessageInteractionResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: 'discord_typings.APIInteractionTypes'
    name: str
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    name_localized: NotRequired[Union[str, None]]


class APIMessageMentionChannelResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    type: 'discord_typings.APIChannelTypes'
    guild_id: 'discord_typings.APISnowflake'


class APIMessageReactionCountDetailsResponse(TypedDict):
    burst: int
    normal: int


class APIMessageReactionEmojiResponse(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    name: NotRequired[Union[str, None]]
    animated: NotRequired[Union[bool, None]]


class APIMessageReactionResponse(TypedDict):
    emoji: 'discord_typings.APIMessageReactionEmojiResponse'
    count: int
    count_details: 'discord_typings.APIMessageReactionCountDetailsResponse'
    burst_colors: list[str]
    me_burst: bool
    me: bool


class APIMessageReferenceRequest(TypedDict):
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    message_id: 'discord_typings.APISnowflake'
    fail_if_not_exists: NotRequired[Union[bool, None]]
    type: NotRequired[Union[None, 'discord_typings.APIMessageReferenceType']]


class APIMessageReferenceResponse(TypedDict):
    type: NotRequired[Union[None, 'discord_typings.APIMessageReferenceType']]
    channel_id: 'discord_typings.APISnowflake'
    message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


APIMessageReferenceType = Literal[
    0,
]


class APIMessageResponse(TypedDict):
    type: 'discord_typings.APIMessageType'
    content: str
    mentions: list['discord_typings.APIUserResponse']
    mention_roles: list['discord_typings.APISnowflake']
    attachments: list['discord_typings.APIMessageAttachmentResponse']
    embeds: list['discord_typings.APIMessageEmbedResponse']
    timestamp: str
    edited_timestamp: NotRequired[Union[str, None]]
    flags: int
    components: list['discord_typings.APIActionRowComponentResponse']
    resolved: NotRequired[Union[None, 'discord_typings.APIResolvedObjectsResponse']]
    stickers: NotRequired[Union[list[Union['discord_typings.APIGuildStickerResponse', 'discord_typings.APIStandardStickerResponse']], None]]
    sticker_items: NotRequired[Union[list['discord_typings.APIMessageStickerItemResponse'], None]]
    id: 'discord_typings.APISnowflake'
    channel_id: 'discord_typings.APISnowflake'
    author: 'discord_typings.APIUserResponse'
    pinned: bool
    mention_everyone: bool
    tts: bool
    call: NotRequired[Union[None, 'discord_typings.APIMessageCallResponse']]
    activity: NotRequired[Union[None, 'discord_typings.APIMessageActivityResponse']]
    application: NotRequired[Union[None, 'discord_typings.APIBasicApplicationResponse']]
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    interaction: NotRequired[Union[None, 'discord_typings.APIMessageInteractionResponse']]
    nonce: NotRequired[Union[int, str, None]]
    webhook_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    message_reference: NotRequired[Union[None, 'discord_typings.APIMessageReferenceResponse']]
    thread: NotRequired[Union[None, 'discord_typings.APIThreadResponse']]
    mention_channels: NotRequired[Union[list[Union[None, 'discord_typings.APIMessageMentionChannelResponse']], None]]
    role_subscription_data: NotRequired[Union[None, 'discord_typings.APIMessageRoleSubscriptionDataResponse']]
    purchase_notification: NotRequired[Union[None, 'discord_typings.APIPurchaseNotificationResponse']]
    position: NotRequired[Union[int, None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollResponse']]
    interaction_metadata: NotRequired[Union['discord_typings.APIApplicationCommandInteractionMetadataResponse', 'discord_typings.APIMessageComponentInteractionMetadataResponse', 'discord_typings.APIModalSubmitInteractionMetadataResponse', None]]
    message_snapshots: NotRequired[Union[list['discord_typings.APIMessageSnapshotResponse'], None]]
    reactions: NotRequired[Union[list['discord_typings.APIMessageReactionResponse'], None]]
    referenced_message: NotRequired[Union[None, 'discord_typings.APIBasicMessageResponse']]


class APIMessageRoleSubscriptionDataResponse(TypedDict):
    role_subscription_listing_id: 'discord_typings.APISnowflake'
    tier_name: str
    total_months_subscribed: int
    is_renewal: bool


class APIMessageSnapshotResponse(TypedDict):
    message: NotRequired[Union[None, 'discord_typings.APIMinimalContentMessageResponse']]


class APIMessageStickerItemResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    format_type: 'discord_typings.APIStickerFormatTypes'


APIMessageType = Literal[
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    31,
    32,
    36,
    37,
    38,
    39,
    55,
]


APIMetadataItemTypes = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]


class APIMinimalContentMessageResponse(TypedDict):
    type: 'discord_typings.APIMessageType'
    content: str
    mentions: list['discord_typings.APIUserResponse']
    mention_roles: list['discord_typings.APISnowflake']
    attachments: list['discord_typings.APIMessageAttachmentResponse']
    embeds: list['discord_typings.APIMessageEmbedResponse']
    timestamp: str
    edited_timestamp: NotRequired[Union[str, None]]
    flags: int
    components: list['discord_typings.APIActionRowComponentResponse']
    resolved: NotRequired[Union[None, 'discord_typings.APIResolvedObjectsResponse']]
    stickers: NotRequired[Union[list[Union['discord_typings.APIGuildStickerResponse', 'discord_typings.APIStandardStickerResponse']], None]]
    sticker_items: NotRequired[Union[list['discord_typings.APIMessageStickerItemResponse'], None]]


class APIModalInteractionCallbackRequest(TypedDict):
    type: Literal[9]
    data: 'discord_typings.APIModalInteractionCallbackRequestData'


class APIModalInteractionCallbackRequestData(TypedDict):
    custom_id: str
    title: str
    components: list['discord_typings.APIActionRowComponentForModalRequest']


class APIModalSubmitInteractionMetadataResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[5]
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    authorizing_integration_owners: dict[str, 'discord_typings.APISnowflake']
    original_response_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    triggering_interaction_metadata: Union['discord_typings.APIApplicationCommandInteractionMetadataResponse', 'discord_typings.APIMessageComponentInteractionMetadataResponse']


class APIMyGuildResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    banner: NotRequired[Union[str, None]]
    owner: bool
    permissions: str
    features: list['discord_typings.APIGuildFeatures']
    approximate_member_count: NotRequired[Union[int, None]]
    approximate_presence_count: NotRequired[Union[int, None]]


APINameplatePalette = Literal[
]


class APINewMemberActionResponse(TypedDict):
    channel_id: 'discord_typings.APISnowflake'
    action_type: 'discord_typings.APINewMemberActionType'
    title: str
    description: str
    emoji: NotRequired[Union[None, 'discord_typings.APISettingsEmojiResponse']]
    icon: NotRequired[Union[str, None]]


APINewMemberActionType = Literal[
    0,
    1,
]


class APIOAuth2GetAuthorizationResponse(TypedDict):
    application: 'discord_typings.APIApplicationResponse'
    expires: str
    scopes: list['discord_typings.APIOAuth2Scopes']
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


class APIOAuth2GetKeys(TypedDict):
    keys: list['discord_typings.APIOAuth2Key']


class APIOAuth2GetOpenIDConnectUserInfoResponse(TypedDict):
    sub: str
    email: NotRequired[Union[str, None]]
    email_verified: NotRequired[Union[bool, None]]
    preferred_username: NotRequired[Union[str, None]]
    nickname: NotRequired[Union[str, None]]
    picture: NotRequired[Union[str, None]]
    locale: NotRequired[Union[str, None]]


class APIOAuth2Key(TypedDict):
    kty: str
    use: str
    kid: str
    n: str
    e: str
    alg: str


APIOAuth2Scopes = Literal[
    'identify',
    'email',
    'connections',
    'guilds',
    'guilds.join',
    'guilds.members.read',
    'gdm.join',
    'bot',
    'rpc',
    'rpc.notifications.read',
    'rpc.voice.read',
    'rpc.voice.write',
    'rpc.video.read',
    'rpc.video.write',
    'rpc.screenshare.read',
    'rpc.screenshare.write',
    'rpc.activities.write',
    'webhook.incoming',
    'messages.read',
    'applications.builds.upload',
    'applications.builds.read',
    'applications.commands',
    'applications.commands.permissions.update',
    'applications.commands.update',
    'applications.store.update',
    'applications.entitlements',
    'activities.read',
    'activities.write',
    'activities.invites.write',
    'relationships.read',
    'voice',
    'dm_channels.read',
    'role_connections.write',
    'openid',
]


class APIOnboardingPromptOptionRequest(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    title: str
    description: NotRequired[Union[str, None]]
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]
    emoji_animated: NotRequired[Union[bool, None]]
    role_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    channel_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]


class APIOnboardingPromptOptionResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    title: str
    description: str
    emoji: 'discord_typings.APISettingsEmojiResponse'
    role_ids: list['discord_typings.APISnowflake']
    channel_ids: list['discord_typings.APISnowflake']


class APIOnboardingPromptResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    title: str
    options: list['discord_typings.APIOnboardingPromptOptionResponse']
    single_select: bool
    required: bool
    in_onboarding: bool
    type: 'discord_typings.APIOnboardingPromptType'


APIOnboardingPromptType = Literal[
    0,
    1,
]


class APIPartialDiscordIntegrationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal['discord']
    name: NotRequired[Union[str, None]]
    account: NotRequired[Union[None, 'discord_typings.APIAccountResponse']]
    application_id: 'discord_typings.APISnowflake'


class APIPartialExternalConnectionIntegrationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal['twitch', 'youtube']
    name: NotRequired[Union[str, None]]
    account: NotRequired[Union[None, 'discord_typings.APIAccountResponse']]


class APIPartialGuildSubscriptionIntegrationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal['guild_subscription']
    name: NotRequired[Union[str, None]]
    account: NotRequired[Union[None, 'discord_typings.APIAccountResponse']]


class APIPollAnswerCreateRequest(TypedDict):
    poll_media: 'discord_typings.APIPollMediaCreateRequest'


class APIPollAnswerDetailsResponse(TypedDict):
    users: NotRequired[Union[list['discord_typings.APIUserResponse'], None]]


class APIPollAnswerResponse(TypedDict):
    answer_id: int
    poll_media: 'discord_typings.APIPollMediaResponse'


class APIPollCreateRequest(TypedDict):
    question: 'discord_typings.APIPollMedia'
    answers: list['discord_typings.APIPollAnswerCreateRequest']
    allow_multiselect: NotRequired[Union[bool, None]]
    layout_type: NotRequired[Union[None, 'discord_typings.APIPollLayoutTypes']]
    duration: NotRequired[Union[int, None]]


class APIPollEmoji(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    name: NotRequired[Union[str, None]]
    animated: NotRequired[Union[bool, None]]


class APIPollEmojiCreateRequest(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    name: NotRequired[Union[str, None]]
    animated: NotRequired[Union[bool, None]]


APIPollLayoutTypes = Literal[
]


class APIPollMedia(TypedDict):
    text: NotRequired[Union[str, None]]
    emoji: NotRequired[Union[None, 'discord_typings.APIPollEmoji']]


class APIPollMediaCreateRequest(TypedDict):
    text: NotRequired[Union[str, None]]
    emoji: NotRequired[Union[None, 'discord_typings.APIPollEmojiCreateRequest']]


class APIPollMediaResponse(TypedDict):
    text: NotRequired[Union[str, None]]
    emoji: NotRequired[Union[None, 'discord_typings.APIMessageReactionEmojiResponse']]


class APIPollResponse(TypedDict):
    question: 'discord_typings.APIPollMediaResponse'
    answers: list['discord_typings.APIPollAnswerResponse']
    expiry: str
    allow_multiselect: bool
    layout_type: 'discord_typings.APIPollLayoutTypes'
    results: 'discord_typings.APIPollResultsResponse'


class APIPollResultsEntryResponse(TypedDict):
    id: int
    count: int
    me_voted: NotRequired[Union[bool, None]]


class APIPollResultsResponse(TypedDict):
    answer_counts: NotRequired[Union[list['discord_typings.APIPollResultsEntryResponse'], None]]
    is_finalized: bool


class APIPongInteractionCallbackRequest(TypedDict):
    type: Literal[1]


APIPremiumGuildTiers = Literal[
    0,
    1,
    2,
    3,
]


APIPremiumTypes = Literal[
    0,
    1,
    2,
    3,
]


class APIPrivateApplicationResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    icon: NotRequired[Union[str, None]]
    description: str
    type: NotRequired[Union[None, 'discord_typings.APIApplicationTypes']]
    cover_image: NotRequired[Union[str, None]]
    primary_sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    bot: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    slug: NotRequired[Union[str, None]]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    rpc_origins: NotRequired[Union[list[Union[str, None]], None]]
    bot_public: NotRequired[Union[bool, None]]
    bot_require_code_grant: NotRequired[Union[bool, None]]
    terms_of_service_url: NotRequired[Union[str, None]]
    privacy_policy_url: NotRequired[Union[str, None]]
    custom_install_url: NotRequired[Union[str, None]]
    install_params: NotRequired[Union[None, 'discord_typings.APIApplicationOAuth2InstallParamsResponse']]
    integration_types_config: NotRequired[Union[dict[str, 'discord_typings.APIApplicationIntegrationTypeConfigurationResponse'], None]]
    verify_key: str
    flags: int
    max_participants: NotRequired[Union[int, None]]
    tags: NotRequired[Union[list[str], None]]
    redirect_uris: list[Union[str, None]]
    interactions_endpoint_url: NotRequired[Union[str, None]]
    role_connections_verification_url: NotRequired[Union[str, None]]
    owner: 'discord_typings.APIUserResponse'
    approximate_guild_count: NotRequired[Union[int, None]]
    approximate_user_install_count: int
    explicit_content_filter: 'discord_typings.APIApplicationExplicitContentFilterTypes'
    team: NotRequired[Union[None, 'discord_typings.APITeamResponse']]


class APIPrivateChannelLocation(TypedDict):
    id: str
    kind: Literal['pc']
    channel_id: 'discord_typings.APISnowflake'


class APIPrivateChannelResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[1]
    last_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    flags: int
    last_pin_timestamp: NotRequired[Union[str, None]]
    recipients: list['discord_typings.APIUserResponse']


class APIPrivateGroupChannelResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[3]
    last_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    flags: int
    last_pin_timestamp: NotRequired[Union[str, None]]
    recipients: list['discord_typings.APIUserResponse']
    name: NotRequired[Union[str, None]]
    icon: NotRequired[Union[str, None]]
    owner_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    managed: NotRequired[Union[bool, None]]
    application_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIPrivateGuildMemberResponse(TypedDict):
    avatar: NotRequired[Union[str, None]]
    avatar_decoration_data: NotRequired[Union[None, 'discord_typings.APIUserAvatarDecorationResponse']]
    banner: NotRequired[Union[str, None]]
    communication_disabled_until: NotRequired[Union[str, None]]
    flags: int
    joined_at: str
    nick: NotRequired[Union[str, None]]
    pending: bool
    premium_since: NotRequired[Union[str, None]]
    roles: list['discord_typings.APISnowflake']
    user: 'discord_typings.APIUserResponse'
    mute: bool
    deaf: bool


class APIProvisionalTokenResponse(TypedDict):
    token_type: str
    access_token: str
    expires_in: int
    scope: str
    id_token: str
    refresh_token: NotRequired[Union[str, None]]
    scopes: NotRequired[Union[list[str], None]]
    expires_at_s: NotRequired[Union[int, None]]


class APIPurchaseNotificationResponse(TypedDict):
    type: 'discord_typings.APIPurchaseType'
    guild_product_purchase: NotRequired[Union[None, 'discord_typings.APIGuildProductPurchaseResponse']]


APIPurchaseType = Literal[
    0,
]


class APIQuarantineUserAction(TypedDict):
    type: Literal[4]
    metadata: NotRequired[Union[None, 'discord_typings.APIQuarantineUserActionMetadata']]


class APIQuarantineUserActionMetadata(TypedDict):
    pass


class APIQuarantineUserActionMetadataResponse(TypedDict):
    pass


class APIQuarantineUserActionResponse(TypedDict):
    type: Literal[4]
    metadata: 'discord_typings.APIQuarantineUserActionMetadataResponse'


APIReactionTypes = Literal[
    0,
    1,
]


class APIResolvedObjectsResponse(TypedDict):
    users: dict[str, 'discord_typings.APIUserResponse']
    members: dict[str, 'discord_typings.APIGuildMemberResponse']
    channels: dict[str, Union['discord_typings.APIGuildChannelResponse', 'discord_typings.APIPrivateChannelResponse', 'discord_typings.APIPrivateGroupChannelResponse', 'discord_typings.APIThreadResponse']]
    roles: dict[str, 'discord_typings.APIGuildRoleResponse']


class APIResourceChannelResponse(TypedDict):
    channel_id: 'discord_typings.APISnowflake'
    title: str
    emoji: NotRequired[Union[None, 'discord_typings.APISettingsEmojiResponse']]
    icon: NotRequired[Union[str, None]]
    description: str


class APIRichEmbed(TypedDict):
    type: NotRequired[Union[str, None]]
    url: NotRequired[Union[str, None]]
    title: NotRequired[Union[str, None]]
    color: NotRequired[Union[int, None]]
    timestamp: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    author: NotRequired[Union[None, 'discord_typings.APIRichEmbedAuthor']]
    image: NotRequired[Union[None, 'discord_typings.APIRichEmbedImage']]
    thumbnail: NotRequired[Union[None, 'discord_typings.APIRichEmbedThumbnail']]
    footer: NotRequired[Union[None, 'discord_typings.APIRichEmbedFooter']]
    fields: NotRequired[Union[list['discord_typings.APIRichEmbedField'], None]]
    provider: NotRequired[Union[None, 'discord_typings.APIRichEmbedProvider']]
    video: NotRequired[Union[None, 'discord_typings.APIRichEmbedVideo']]


class APIRichEmbedAuthor(TypedDict):
    name: NotRequired[Union[str, None]]
    url: NotRequired[Union[str, None]]
    icon_url: NotRequired[Union[str, None]]


class APIRichEmbedField(TypedDict):
    name: str
    value: str
    inline: NotRequired[Union[bool, None]]


class APIRichEmbedFooter(TypedDict):
    text: NotRequired[Union[str, None]]
    icon_url: NotRequired[Union[str, None]]


class APIRichEmbedImage(TypedDict):
    url: NotRequired[Union[str, None]]
    width: NotRequired[Union[int, None]]
    height: NotRequired[Union[int, None]]
    placeholder: NotRequired[Union[str, None]]
    placeholder_version: NotRequired[Union[int, None]]
    is_animated: NotRequired[Union[bool, None]]


class APIRichEmbedProvider(TypedDict):
    name: NotRequired[Union[str, None]]
    url: NotRequired[Union[str, None]]


class APIRichEmbedThumbnail(TypedDict):
    url: NotRequired[Union[str, None]]
    width: NotRequired[Union[int, None]]
    height: NotRequired[Union[int, None]]
    placeholder: NotRequired[Union[str, None]]
    placeholder_version: NotRequired[Union[int, None]]
    is_animated: NotRequired[Union[bool, None]]


class APIRichEmbedVideo(TypedDict):
    url: NotRequired[Union[str, None]]
    width: NotRequired[Union[int, None]]
    height: NotRequired[Union[int, None]]
    placeholder: NotRequired[Union[str, None]]
    placeholder_version: NotRequired[Union[int, None]]
    is_animated: NotRequired[Union[bool, None]]


class APIRoleSelectComponentForMessageRequest(TypedDict):
    type: Literal[6]
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list['discord_typings.APIRoleSelectDefaultValue'], None]]


class APIRoleSelectComponentResponse(TypedDict):
    type: Literal[6]
    id: int
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list['discord_typings.APIRoleSelectDefaultValueResponse'], None]]


class APIRoleSelectDefaultValue(TypedDict):
    type: Literal['role']
    id: 'discord_typings.APISnowflake'


class APIRoleSelectDefaultValueResponse(TypedDict):
    type: Literal['role']
    id: 'discord_typings.APISnowflake'


class APISDKMessageRequest(TypedDict):
    content: NotRequired[Union[str, None]]
    embeds: NotRequired[Union[list['discord_typings.APIRichEmbed'], None]]
    allowed_mentions: NotRequired[Union[None, 'discord_typings.APIMessageAllowedMentionsRequest']]
    sticker_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    components: NotRequired[Union[list['discord_typings.APIActionRowComponentForMessageRequest'], None]]
    flags: NotRequired[Union[int, None]]
    attachments: NotRequired[Union[list['discord_typings.APIMessageAttachmentRequest'], None]]
    poll: NotRequired[Union[None, 'discord_typings.APIPollCreateRequest']]
    confetti_potion: NotRequired[Union[None, 'discord_typings.APIConfettiPotionCreateRequest']]
    message_reference: NotRequired[Union[None, 'discord_typings.APIMessageReferenceRequest']]
    nonce: NotRequired[Union[int, str, None]]
    enforce_nonce: NotRequired[Union[bool, None]]
    tts: NotRequired[Union[bool, None]]


class APIScheduledEventResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    name: str
    description: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    status: 'discord_typings.APIGuildScheduledEventStatuses'
    entity_type: 'discord_typings.APIGuildScheduledEventEntityTypes'
    entity_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    user_count: NotRequired[Union[int, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    user_rsvp: NotRequired[Union[None, 'discord_typings.APIScheduledEventUserResponse']]


class APIScheduledEventUserResponse(TypedDict):
    guild_scheduled_event_id: 'discord_typings.APISnowflake'
    user_id: 'discord_typings.APISnowflake'
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    member: NotRequired[Union[None, 'discord_typings.APIGuildMemberResponse']]


class APISettingsEmojiResponse(TypedDict):
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    name: NotRequired[Union[str, None]]
    animated: NotRequired[Union[bool, None]]


class APISlackWebhook(TypedDict):
    text: NotRequired[Union[str, None]]
    username: NotRequired[Union[str, None]]
    icon_url: NotRequired[Union[str, None]]
    attachments: NotRequired[Union[list['discord_typings.APIWebhookSlackEmbed'], None]]


APISnowflakeSelectDefaultValueTypes = Literal[
    'user',
    'role',
    'channel',
]


APISortingOrder = Literal[
    'asc',
    'desc',
]


class APISoundboardCreateRequest(TypedDict):
    name: str
    volume: NotRequired[Union[float, None]]
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]
    sound: str


class APISoundboardPatchRequestPartial(TypedDict):
    name: NotRequired[str]
    volume: NotRequired[Union[float, None]]
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]


class APISoundboardSoundResponse(TypedDict):
    name: str
    sound_id: 'discord_typings.APISnowflake'
    volume: float
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    available: bool
    user: NotRequired[Union[None, 'discord_typings.APIUserResponse']]


class APISoundboardSoundSendRequest(TypedDict):
    sound_id: 'discord_typings.APISnowflake'
    source_guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APISpamLinkRuleResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    creator_id: 'discord_typings.APISnowflake'
    name: str
    event_type: 'discord_typings.APIAutomodEventType'
    actions: list[Union['discord_typings.APIBlockMessageActionResponse', 'discord_typings.APIFlagToChannelActionResponse', 'discord_typings.APIQuarantineUserActionResponse', 'discord_typings.APIUserCommunicationDisabledActionResponse']]
    trigger_type: Literal[2]
    enabled: NotRequired[Union[bool, None]]
    exempt_roles: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    exempt_channels: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    trigger_metadata: 'discord_typings.APISpamLinkTriggerMetadataResponse'


class APISpamLinkTriggerMetadataResponse(TypedDict):
    pass


class APIStageInstanceResponse(TypedDict):
    guild_id: 'discord_typings.APISnowflake'
    channel_id: 'discord_typings.APISnowflake'
    topic: str
    privacy_level: 'discord_typings.APIStageInstancesPrivacyLevels'
    id: 'discord_typings.APISnowflake'
    discoverable_disabled: NotRequired[Union[bool, None]]
    guild_scheduled_event_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


APIStageInstancesPrivacyLevels = Literal[
    1,
    2,
]


class APIStageScheduledEventCreateRequest(TypedDict):
    name: str
    description: NotRequired[Union[str, None]]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    entity_type: Literal[1]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    entity_metadata: NotRequired[Union[None, 'discord_typings.APIEntityMetadataStageInstance']]


class APIStageScheduledEventPatchRequestPartial(TypedDict):
    status: NotRequired[Union[None, 'discord_typings.APIGuildScheduledEventStatuses']]
    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: NotRequired[str]
    scheduled_end_time: NotRequired[Union[str, None]]
    entity_type: NotRequired[Union[None, Literal[1]]]
    privacy_level: NotRequired['discord_typings.APIGuildScheduledEventPrivacyLevels']
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    entity_metadata: NotRequired[Union[None, 'discord_typings.APIEntityMetadataStageInstance']]


class APIStageScheduledEventResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    name: str
    description: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    status: 'discord_typings.APIGuildScheduledEventStatuses'
    entity_type: Literal[1]
    entity_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    user_count: NotRequired[Union[int, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    user_rsvp: NotRequired[Union[None, 'discord_typings.APIScheduledEventUserResponse']]
    entity_metadata: NotRequired[Union[None, 'discord_typings.APIEntityMetadataStageInstanceResponse']]


class APIStandardStickerResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    tags: str
    type: Literal[1]
    format_type: NotRequired[Union[None, 'discord_typings.APIStickerFormatTypes']]
    description: NotRequired[Union[str, None]]
    pack_id: 'discord_typings.APISnowflake'
    sort_value: int


APIStickerFormatTypes = Literal[
    1,
    2,
    3,
    4,
]


class APIStickerPackCollectionResponse(TypedDict):
    sticker_packs: list['discord_typings.APIStickerPackResponse']


class APIStickerPackResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    sku_id: 'discord_typings.APISnowflake'
    name: str
    description: NotRequired[Union[str, None]]
    stickers: list['discord_typings.APIStandardStickerResponse']
    cover_sticker_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    banner_asset_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


APIStickerTypes = Literal[
    1,
    2,
]


class APIStringSelectComponentForMessageRequest(TypedDict):
    type: Literal[3]
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    options: list['discord_typings.APIStringSelectOptionForMessageRequest']


class APIStringSelectComponentResponse(TypedDict):
    type: Literal[3]
    id: int
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    options: list['discord_typings.APIStringSelectOptionResponse']


class APIStringSelectOptionForMessageRequest(TypedDict):
    label: str
    value: str
    description: NotRequired[Union[str, None]]
    default: NotRequired[Union[bool, None]]
    emoji: NotRequired[Union[None, 'discord_typings.APIComponentEmojiForMessageRequest']]


class APIStringSelectOptionResponse(TypedDict):
    label: str
    value: str
    description: NotRequired[Union[str, None]]
    emoji: NotRequired[Union[None, 'discord_typings.APIComponentEmojiResponse']]
    default: NotRequired[Union[bool, None]]


class APITeamMemberResponse(TypedDict):
    user: 'discord_typings.APIUserResponse'
    team_id: 'discord_typings.APISnowflake'
    membership_state: 'discord_typings.APITeamMembershipStates'


APITeamMembershipStates = Literal[
    1,
    2,
]


class APITeamResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    icon: NotRequired[Union[str, None]]
    name: str
    owner_user_id: 'discord_typings.APISnowflake'
    members: list['discord_typings.APITeamMemberResponse']


class APITextInputComponentForModalRequest(TypedDict):
    type: Literal[4]
    custom_id: str
    style: 'discord_typings.APITextInputStyleTypes'
    label: str
    value: NotRequired[Union[str, None]]
    placeholder: NotRequired[Union[str, None]]
    required: NotRequired[Union[bool, None]]
    min_length: NotRequired[Union[int, None]]
    max_length: NotRequired[Union[int, None]]


class APITextInputComponentResponse(TypedDict):
    type: Literal[4]
    id: int
    custom_id: str
    style: 'discord_typings.APITextInputStyleTypes'
    label: NotRequired[Union[str, None]]
    value: NotRequired[Union[str, None]]
    placeholder: NotRequired[Union[str, None]]
    required: NotRequired[Union[bool, None]]
    min_length: NotRequired[Union[int, None]]
    max_length: NotRequired[Union[int, None]]


APITextInputStyleTypes = Literal[
    1,
    2,
]


APIThreadAutoArchiveDuration = Literal[
    60,
    1440,
    4320,
    10080,
]


class APIThreadMemberResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    user_id: 'discord_typings.APISnowflake'
    join_timestamp: str
    flags: int
    member: NotRequired[Union[None, 'discord_typings.APIGuildMemberResponse']]


class APIThreadMetadataResponse(TypedDict):
    archived: bool
    archive_timestamp: NotRequired[Union[str, None]]
    auto_archive_duration: 'discord_typings.APIThreadAutoArchiveDuration'
    locked: bool
    create_timestamp: NotRequired[Union[str, None]]
    invitable: NotRequired[Union[bool, None]]


class APIThreadResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    type: Literal[10, 11, 12]
    last_message_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    flags: int
    last_pin_timestamp: NotRequired[Union[str, None]]
    guild_id: 'discord_typings.APISnowflake'
    name: str
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    rate_limit_per_user: NotRequired[Union[int, None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]
    permissions: NotRequired[Union[str, None]]
    owner_id: 'discord_typings.APISnowflake'
    thread_metadata: NotRequired[Union[None, 'discord_typings.APIThreadMetadataResponse']]
    message_count: int
    member_count: int
    total_message_sent: int
    applied_tags: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    member: NotRequired[Union[None, 'discord_typings.APIThreadMemberResponse']]


class APIThreadSearchResponse(TypedDict):
    threads: list['discord_typings.APIThreadResponse']
    members: list['discord_typings.APIThreadMemberResponse']
    has_more: NotRequired[Union[bool, None]]
    first_messages: NotRequired[Union[list['discord_typings.APIMessageResponse'], None]]
    total_results: NotRequired[Union[int, None]]


APIThreadSearchTagSetting = Literal[
]


APIThreadSortOrder = Literal[
    0,
    1,
]


APIThreadSortingMode = Literal[
    'relevance',
    'creation_time',
    'last_message_time',
    'archive_time',
]


class APIThreadsResponse(TypedDict):
    threads: list['discord_typings.APIThreadResponse']
    members: list['discord_typings.APIThreadMemberResponse']
    has_more: NotRequired[Union[bool, None]]
    first_messages: NotRequired[Union[list['discord_typings.APIMessageResponse'], None]]


class APITypingIndicatorResponse(TypedDict):
    pass


class APIUpdateDMRequestPartial(TypedDict):
    name: NotRequired[Union[str, None]]


class APIUpdateDefaultReactionEmojiRequest(TypedDict):
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]


class APIUpdateGroupDMRequestPartial(TypedDict):
    name: NotRequired[Union[str, None]]
    icon: NotRequired[Union[str, None]]


class APIUpdateGuildChannelRequestPartial(TypedDict):
    type: NotRequired[Union[None, Literal[0, 2, 4, 5, 13, 14, 15]]]
    name: NotRequired[str]
    position: NotRequired[Union[int, None]]
    topic: NotRequired[Union[str, None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    nsfw: NotRequired[Union[bool, None]]
    rate_limit_per_user: NotRequired[Union[int, None]]
    parent_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    permission_overwrites: NotRequired[Union[list['discord_typings.APIChannelPermissionOverwriteRequest'], None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]
    default_auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    default_reaction_emoji: NotRequired[Union[None, 'discord_typings.APIUpdateDefaultReactionEmojiRequest']]
    default_thread_rate_limit_per_user: NotRequired[Union[int, None]]
    default_sort_order: NotRequired[Union[None, 'discord_typings.APIThreadSortOrder']]
    default_forum_layout: NotRequired[Union[None, 'discord_typings.APIForumLayout']]
    flags: NotRequired[Union[int, None]]
    available_tags: NotRequired[Union[list['discord_typings.APIUpdateThreadTagRequest'], None]]


class APIUpdateGuildOnboardingRequest(TypedDict):
    prompts: NotRequired[Union[list['discord_typings.APIUpdateOnboardingPromptRequest'], None]]
    enabled: NotRequired[Union[bool, None]]
    default_channel_ids: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    mode: NotRequired[Union[None, 'discord_typings.APIGuildOnboardingMode']]


class APIUpdateMessageInteractionCallbackRequest(TypedDict):
    type: Literal[6, 7]
    data: NotRequired[Union[None, 'discord_typings.APIIncomingWebhookUpdateForInteractionCallbackRequestPartial']]


class APIUpdateMessageInteractionCallbackResponse(TypedDict):
    type: Literal[7]
    message: 'discord_typings.APIMessageResponse'


class APIUpdateOnboardingPromptRequest(TypedDict):
    title: str
    options: list['discord_typings.APIOnboardingPromptOptionRequest']
    single_select: NotRequired[Union[bool, None]]
    required: NotRequired[Union[bool, None]]
    in_onboarding: NotRequired[Union[bool, None]]
    type: NotRequired[Union[None, 'discord_typings.APIOnboardingPromptType']]
    id: 'discord_typings.APISnowflake'


class APIUpdateThreadRequestPartial(TypedDict):
    name: NotRequired[Union[str, None]]
    archived: NotRequired[Union[bool, None]]
    locked: NotRequired[Union[bool, None]]
    invitable: NotRequired[Union[bool, None]]
    auto_archive_duration: NotRequired[Union[None, 'discord_typings.APIThreadAutoArchiveDuration']]
    rate_limit_per_user: NotRequired[Union[int, None]]
    flags: NotRequired[Union[int, None]]
    applied_tags: NotRequired[Union[list['discord_typings.APISnowflake'], None]]
    bitrate: NotRequired[Union[int, None]]
    user_limit: NotRequired[Union[int, None]]
    rtc_region: NotRequired[Union[str, None]]
    video_quality_mode: NotRequired[Union[None, 'discord_typings.APIVideoQualityModes']]


class APIUpdateThreadTagRequest(TypedDict):
    name: str
    emoji_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    emoji_name: NotRequired[Union[str, None]]
    moderated: NotRequired[Union[bool, None]]
    id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIUserAvatarDecorationResponse(TypedDict):
    asset: str
    sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIUserCollectiblesResponse(TypedDict):
    nameplate: NotRequired[Union[None, 'discord_typings.APIUserNameplateResponse']]


class APIUserCommunicationDisabledAction(TypedDict):
    type: Literal[3]
    metadata: 'discord_typings.APIUserCommunicationDisabledActionMetadata'


class APIUserCommunicationDisabledActionMetadata(TypedDict):
    duration_seconds: NotRequired[Union[int, None]]


class APIUserCommunicationDisabledActionMetadataResponse(TypedDict):
    duration_seconds: int


class APIUserCommunicationDisabledActionResponse(TypedDict):
    type: Literal[3]
    metadata: 'discord_typings.APIUserCommunicationDisabledActionMetadataResponse'


class APIUserGuildOnboardingResponse(TypedDict):
    guild_id: 'discord_typings.APISnowflake'
    prompts: list['discord_typings.APIOnboardingPromptResponse']
    default_channel_ids: list['discord_typings.APISnowflake']
    enabled: bool


class APIUserNameplateResponse(TypedDict):
    sku_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    asset: NotRequired[Union[str, None]]
    label: NotRequired[Union[str, None]]
    palette: NotRequired[Union[None, 'discord_typings.APINameplatePalette']]


APIUserNotificationSettings = Literal[
    0,
    1,
]


class APIUserPIIResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    username: str
    avatar: NotRequired[Union[str, None]]
    discriminator: str
    public_flags: int
    flags: int
    bot: NotRequired[Union[bool, None]]
    system: NotRequired[Union[bool, None]]
    banner: NotRequired[Union[str, None]]
    accent_color: NotRequired[Union[int, None]]
    global_name: NotRequired[Union[str, None]]
    avatar_decoration_data: NotRequired[Union[None, 'discord_typings.APIUserAvatarDecorationResponse']]
    collectibles: NotRequired[Union[None, 'discord_typings.APIUserCollectiblesResponse']]
    clan: NotRequired[Union[None, 'discord_typings.APIUserPrimaryGuildResponse']]
    mfa_enabled: bool
    locale: 'discord_typings.APIAvailableLocalesEnum'
    premium_type: NotRequired[Union[None, 'discord_typings.APIPremiumTypes']]
    email: NotRequired[Union[str, None]]
    verified: NotRequired[Union[bool, None]]


class APIUserPrimaryGuildResponse(TypedDict):
    pass


class APIUserResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    username: str
    avatar: NotRequired[Union[str, None]]
    discriminator: str
    public_flags: int
    flags: int
    bot: NotRequired[Union[bool, None]]
    system: NotRequired[Union[bool, None]]
    banner: NotRequired[Union[str, None]]
    accent_color: NotRequired[Union[int, None]]
    global_name: NotRequired[Union[str, None]]
    avatar_decoration_data: NotRequired[Union[None, 'discord_typings.APIUserAvatarDecorationResponse']]
    collectibles: NotRequired[Union[None, 'discord_typings.APIUserCollectiblesResponse']]
    clan: NotRequired[Union[None, 'discord_typings.APIUserPrimaryGuildResponse']]


class APIUserSelectComponentForMessageRequest(TypedDict):
    type: Literal[5]
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list['discord_typings.APIUserSelectDefaultValue'], None]]


class APIUserSelectComponentResponse(TypedDict):
    type: Literal[5]
    id: int
    custom_id: str
    placeholder: NotRequired[Union[str, None]]
    min_values: NotRequired[Union[int, None]]
    max_values: NotRequired[Union[int, None]]
    disabled: NotRequired[Union[bool, None]]
    default_values: NotRequired[Union[list['discord_typings.APIUserSelectDefaultValueResponse'], None]]


class APIUserSelectDefaultValue(TypedDict):
    type: Literal['user']
    id: 'discord_typings.APISnowflake'


class APIUserSelectDefaultValueResponse(TypedDict):
    type: Literal['user']
    id: 'discord_typings.APISnowflake'


class APIVanityURLErrorResponse(TypedDict):
    message: str
    code: int


class APIVanityURLResponse(TypedDict):
    code: NotRequired[Union[str, None]]
    uses: int
    error: NotRequired[Union[None, 'discord_typings.APIVanityURLErrorResponse']]


APIVerificationLevels = Literal[
    0,
    1,
    2,
    3,
    4,
]


APIVideoQualityModes = Literal[
    1,
    2,
]


class APIVoiceRegionResponse(TypedDict):
    id: str
    name: str
    custom: bool
    deprecated: bool
    optimal: bool


class APIVoiceScheduledEventCreateRequest(TypedDict):
    name: str
    description: NotRequired[Union[str, None]]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    entity_type: Literal[2]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    entity_metadata: NotRequired[Union[None, 'discord_typings.APIEntityMetadataVoice']]


class APIVoiceScheduledEventPatchRequestPartial(TypedDict):
    status: NotRequired[Union[None, 'discord_typings.APIGuildScheduledEventStatuses']]
    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: NotRequired[str]
    scheduled_end_time: NotRequired[Union[str, None]]
    entity_type: NotRequired[Union[None, Literal[2]]]
    privacy_level: NotRequired['discord_typings.APIGuildScheduledEventPrivacyLevels']
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    entity_metadata: NotRequired[Union[None, 'discord_typings.APIEntityMetadataVoice']]


class APIVoiceScheduledEventResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    guild_id: 'discord_typings.APISnowflake'
    name: str
    description: NotRequired[Union[str, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    creator: NotRequired[Union[None, 'discord_typings.APIUserResponse']]
    image: NotRequired[Union[str, None]]
    scheduled_start_time: str
    scheduled_end_time: NotRequired[Union[str, None]]
    status: 'discord_typings.APIGuildScheduledEventStatuses'
    entity_type: Literal[2]
    entity_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    user_count: NotRequired[Union[int, None]]
    privacy_level: 'discord_typings.APIGuildScheduledEventPrivacyLevels'
    user_rsvp: NotRequired[Union[None, 'discord_typings.APIScheduledEventUserResponse']]
    entity_metadata: NotRequired[Union[None, 'discord_typings.APIEntityMetadataVoiceResponse']]


class APIVoiceStateResponse(TypedDict):
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    deaf: bool
    guild_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]
    member: NotRequired[Union[None, 'discord_typings.APIGuildMemberResponse']]
    mute: bool
    request_to_speak_timestamp: NotRequired[Union[str, None]]
    suppress: bool
    self_stream: NotRequired[Union[bool, None]]
    self_deaf: bool
    self_mute: bool
    self_video: bool
    session_id: str
    user_id: 'discord_typings.APISnowflake'


class APIWebhookSlackEmbed(TypedDict):
    title: NotRequired[Union[str, None]]
    title_link: NotRequired[Union[str, None]]
    text: NotRequired[Union[str, None]]
    color: NotRequired[Union[str, None]]
    ts: NotRequired[Union[int, None]]
    pretext: NotRequired[Union[str, None]]
    footer: NotRequired[Union[str, None]]
    footer_icon: NotRequired[Union[str, None]]
    author_name: NotRequired[Union[str, None]]
    author_link: NotRequired[Union[str, None]]
    author_icon: NotRequired[Union[str, None]]
    image_url: NotRequired[Union[str, None]]
    thumb_url: NotRequired[Union[str, None]]
    fields: NotRequired[Union[list['discord_typings.APIWebhookSlackEmbedField'], None]]


class APIWebhookSlackEmbedField(TypedDict):
    name: NotRequired[Union[str, None]]
    value: NotRequired[Union[str, None]]
    inline: NotRequired[Union[bool, None]]


class APIWebhookSourceChannelResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str


class APIWebhookSourceGuildResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    icon: NotRequired[Union[str, None]]
    name: str


APIWebhookTypes = Literal[
    1,
    2,
    3,
]


class APIWelcomeMessageResponse(TypedDict):
    author_ids: list['discord_typings.APISnowflake']
    message: str


class APIWelcomeScreenPatchRequestPartial(TypedDict):
    description: NotRequired[Union[str, None]]
    welcome_channels: NotRequired[Union[list['discord_typings.APIGuildWelcomeChannel'], None]]
    enabled: NotRequired[Union[bool, None]]


class APIWidgetActivity(TypedDict):
    name: str


class APIWidgetChannel(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    position: int


APIWidgetImageStyles = Literal[
    'shield',
    'banner1',
    'banner2',
    'banner3',
    'banner4',
]


class APIWidgetMember(TypedDict):
    id: str
    username: str
    discriminator: 'discord_typings.APIWidgetUserDiscriminator'
    avatar: NotRequired[None]
    status: str
    avatar_url: str
    activity: NotRequired[Union[None, 'discord_typings.APIWidgetActivity']]
    deaf: NotRequired[Union[bool, None]]
    mute: NotRequired[Union[bool, None]]
    self_deaf: NotRequired[Union[bool, None]]
    self_mute: NotRequired[Union[bool, None]]
    suppress: NotRequired[Union[bool, None]]
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


class APIWidgetResponse(TypedDict):
    id: 'discord_typings.APISnowflake'
    name: str
    instant_invite: NotRequired[Union[str, None]]
    channels: list['discord_typings.APIWidgetChannel']
    members: list['discord_typings.APIWidgetMember']
    presence_count: int


class APIWidgetSettingsResponse(TypedDict):
    enabled: bool
    channel_id: NotRequired[Union[None, 'discord_typings.APISnowflake']]


APIWidgetUserDiscriminator = Literal[
    '0000',
]
